#!/usr/bin/env python3
"""AirBnB's `console` module

It defines one class, `HBNBCommand()`, which sub-classes the `cmd.Cmd` class
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""

    prompt = "(hbnb) "

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
        """Override default `empty line + return` behaviour.\n"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
