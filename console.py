#!/usr/bin/python3
"""This module defines the entry point of the command interpreter.

It defines one class, `HBNBCommand()`, which sub-classes the `cmd.Cmd` class.
This module defines abstractions that allows us to manipulate a powerful
storage system (FileStorage / DB). This abstraction will also allow us to
change the type of storage easily without updating all of our codebase.

It allows us to interactively and non-interactively:
    - create a data model
    - manage (create, update, destroy, etc) objects via a console / interpreter
    - store and persist objects to a file (JSON file)

Typical usage example:

    $ ./console
    (hbnb)

    (hbnb) help
    Documented commands (type help <topic>):
    ========================================
    EOF  create  help  quit

    (hbnb)
    (hbnb) quit
    $
"""
import re
import cmd
from models import storage
from models.base_model import BaseModel

current_classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """The command interpreter.

    This class represents the command interpreter, and the control center
    of this project. It defines function handlers for all commands inputted
    in the console and calls the appropriate storage engine APIs to manipulate
    application data / models.

    It sub-classes Python's `cmd.Cmd` class which provides a simple framework
    for writing line-oriented command interpreters.
    """

    prompt = "(hbnb) "

    def precmd(self, line):
        if not line:
            return '\n'

        # matching user input to this format -> `<class>.<command>([<option>])`
        pattern = re.compile(r"([a-zA-Z]+)\.(\w+)\((.*)\)")
        match_list = pattern.findall(line.split()[0])
        instance_objs = storage.all()

        # if no matches were found, hand off execution to default loop
        if not match_list:
            return super().precmd(line)

        # matches come back as a list of a tuple of matched groups.
        # e.g. [('User', 'all', '123-345-567-999')]
        # extract tuple into `match_tuple` variable
        match_tuple = match_list[0]
        # if no <option> was provided, i.e. User.all() vs User.all(<id>)
        if not match_tuple[2]:
            # check if input == <class>.count()
            # checking for this specifically because `do_count()` handler...
            # ...doesn't exist.
            if match_tuple[1] == "count":
                print(len([
                    v for _, v in instance_objs.items()
                    if type(v).__name__ == match_tuple[0]]))
                # trigger the emptyline() method
                return "\n"
            # returning from precmd() hands off the returned string...
            # ...to the main command parser to execute as normal.
            # e.g return "create User" triggers the `create` command...
            # ...with `User` as an argument.
            return "{} {}".format(match_tuple[1], match_tuple[0])
        else:
            # Handles if only one arg was provided between the parenthesis
            # e.g User.show(3509c15a-8862-433c-a97f-56d6cb2e6020)
            args = match_tuple[2].split(", ")
            if len(args) == 1:
                return "{} {} {}".format(match_tuple[1], match_tuple[0], re.sub("[\"\']", "", match_tuple[2]))  # nopep8: E501

        # fallback to default behaviour
        return super().precmd(line)

    def do_help(self, arg):
        """To get help on a command, type help <topic>\n"""
        return super().do_help(arg)

    def do_EOF(self, line):
        """Inbuilt EOF command to gracefully catch errors\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Override default `empty line + return` behaviour\n"""
        pass

    def do_create(self, arg):
        """Creates a new <class name> instance"""
        args = arg.split()
        if not validate_classname(args):
            return

        new_obj = current_classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def help_create(self):
        """Prints the help message for the `create` command"""
        print('\n'.join([
            "Usage: create <class name>",
            "\nCreates a new <class name> instance\n"]))

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()

        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)

        if req_instance is None:
            print("** no instance found **")
            return

        print(req_instance)

    def help_show(self):
        """Prints the help message for the `show` command"""
        print('\n'.join([
            "Usage: show <class name> <id>",
            "\nPrints the string representation of an instance\n"]))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()

        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)

        if req_instance is None:
            print("** no instance found **")
            return

        del instance_objs[key]
        storage.save()

    def help_destroy(self):
        """Prints the help message for the `destroy` command"""
        print('\n'.join([
            "Usage: destroy <class name> <id>",
            "\nDeletes an instance based on the <class name> and <id>\n"]))

    def do_all(self, arg):
        """Prints string representation of all instances based
        or not on the class name
        """
        args = arg.split()
        all_objs = storage.all()

        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
            return
        if args[0] not in current_classes.keys():
            print("** class doesn't exist ** ")
            return
        else:
            print(["{}".format(str(v))
                  for _, v in all_objs.items() if type(v).__name__ == args[0]])
            return

    def help_all(self):
        """Prints the help message for the `all` command"""
        print('\n'.join([
            "Usage: all <classname>",
            "\nPrints a list of str(<class>) for all objects, or objects",
            "matching <class name>\n"]))

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()

        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)

        if req_instance is None:
            print("** no instance found **")
            return

        if not validate_attrs(args):
            return

        if args[2] == "id" or args[2] == "created_at" or args[2] == "updated_at":  # nopep8: E501
            return

        setattr(req_instance, args[2], parse_str(args[3]))
        storage.save()

    def help_update(self):
        """Prints the help message for the `update` command"""
        print('\n'.join([
            "Usage: update <class name> <id> <attribute name> \"<attribute value>\"",  # nopep8: E501
            "\nUpdates an instance based on the <class name> and <id>\n"]))


def validate_classname(args, check_id=False):
    """Runs checks on args to validate classname entry."""
    if len(args) < 1:
        print("** class name missing ** ")
        return False
    if args[0] not in current_classes.keys():
        print("** class doesn't exist ** ")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return False
    return True


def validate_attrs(args):
    """Runs checks on args to validate classname attributes
    and values entry."""
    if len(args) < 3:
        print("** attribute name missing **")
        return False
    if len(args) < 4:
        print("** value missing **")
        return False
    return True


def is_float(x):
    """Checks if `x` is float"""
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True


def is_int(x):
    """Checks if `x` is int"""
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


def parse_str(arg):
    """Parse `arg` to an `int`, `float` or `string`."""
    parsed = re.sub("\"", "", arg)

    if is_int(parsed):
        return int(parsed)
    elif is_float(parsed):
        return float(parsed)
    else:
        return parsed


if __name__ == "__main__":
    HBNBCommand().cmdloop()
