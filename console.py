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
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

current_classes = {'BaseModel': BaseModel, 'User': User,
                   'Amenity': Amenity, 'City': City, 'State': State,
                   'Place': Place, 'Review': Review}


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
        """Defines instructions to execute before <line> is interpreted.
        """
        if not line:
            return '\n'

        pattern = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        match_list = pattern.findall(line)
        if not match_list:
            return super().precmd(line)

        match_tuple = match_list[0]
        if not match_tuple[2]:
            if match_tuple[1] == "count":
                instance_objs = storage.all()
                print(len([
                    v for _, v in instance_objs.items()
                    if type(v).__name__ == match_tuple[0]]))
                return "\n"
            return "{} {}".format(match_tuple[1], match_tuple[0])
        else:
            args = match_tuple[2].split(", ")
            if len(args) == 1:
                return "{} {} {}".format(
                    match_tuple[1], match_tuple[0],
                    re.sub("[\"\']", "", match_tuple[2]))
            else:
                match_json = re.findall(r"{.*}", match_tuple[2])
                if (match_json):
                    return "{} {} {} {}".format(
                        match_tuple[1], match_tuple[0],
                        re.sub("[\"\']", "", args[0]),
                        re.sub("\'", "\"", match_json[0]))
                return "{} {} {} {} {}".format(
                    match_tuple[1], match_tuple[0],
                    re.sub("[\"\']", "", args[0]),
                    re.sub("[\"\']", "", args[1]), args[2])

    def do_help(self, arg):
        """To get help on a command, type help <topic>.
        """
        return super().do_help(arg)

    def do_EOF(self, line):
        """Inbuilt EOF command to gracefully catch errors.
        """
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """Override default `empty line + return` behaviour.
        """
        pass

    def do_create(self, arg):
        """Creates a new instance.
        """
        args = arg.split()
        if not validate_classname(args):
            return

        new_obj = current_classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance.
        """
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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        """
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

    def do_all(self, arg):
        """Prints string representation of all instances.
        """
        args = arg.split()
        all_objs = storage.all()

        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
            return
        if args[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(str(v))
                  for _, v in all_objs.items() if type(v).__name__ == args[0]])
            return

    def do_update(self, arg: str):
        """Updates an instance based on the class name and id.
        """
        args = arg.split(maxsplit=3)
        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return

        match_json = re.findall(r"{.*}", arg)
        if match_json:
            payload = None
            try:
                payload: dict = json.loads(match_json[0])
            except Exception:
                print("** invalid syntax")
                return
            for k, v in payload.items():
                setattr(req_instance, k, v)
            storage.save()
            return
        if not validate_attrs(args):
            return
        first_attr = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        if first_attr:
            setattr(req_instance, args[2], first_attr[0])
        else:
            value_list = args[3].split()
            setattr(req_instance, args[2], parse_str(value_list[0]))
        storage.save()


def validate_classname(args, check_id=False):
    """Runs checks on args to validate classname entry.
    """
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in current_classes.keys():
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return False
    return True


def validate_attrs(args):
    """Runs checks on args to validate classname attributes and values.
    """
    if len(args) < 3:
        print("** attribute name missing **")
        return False
    if len(args) < 4:
        print("** value missing **")
        return False
    return True


def is_float(x):
    """Checks if `x` is float.
    """
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True


def is_int(x):
    """Checks if `x` is int.
    """
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


def parse_str(arg):
    """Parse `arg` to an `int`, `float` or `string`.
    """
    parsed = re.sub("\"", "", arg)

    if is_int(parsed):
        return int(parsed)
    elif is_float(parsed):
        return float(parsed)
    else:
        return arg


if __name__ == "__main__":
    HBNBCommand().cmdloop()
