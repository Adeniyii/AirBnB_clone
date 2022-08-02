#!/usr/bin/env python3
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

Todo:
    * Task 7
    - import completed BaseModel
"""
import cmd
from models import base_model
from models import storage


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
    current_classes = {'BaseModel': base_model.BaseModel}

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

    def do_create(self, arg: str):
        args = arg.split()

        if not validate_classname(args[0]):
            return

        new_obj = self.current_classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def help_create(self):
        print('\n'.join([
            "Usage: create <class>",
            "\nCreates a new <classname> instance\n"]))

    def do_show(self, arg):
        args = arg.split()

        if not validate_classname(args[0]):
            return
        if args[1].strip() == "":
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        instance_objs = storage.all()

        try:
            req_instance = getattr(instance_objs, key)
        except AttributeError:
            print("** no instance found **")
        else:
            print(req_instance)

    def help_show(self):
        print('\n'.join([
            "Usage: show <classname> <id>",
            "\nPrints the string representation of an instance\n"]))


def validate_classname(self, arg):
    """Runs checks on arg to validate classname entry."""
    if arg.strip() == "":
        print("** class name missing **\n")
        return False
    if arg not in self.current_classes.keys():
        print("** class doesn't exist **\n")
        return False
    return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
