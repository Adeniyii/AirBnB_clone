#!/usr/bin/env python3
"""AirBnB's `console` module.

It defines one class, `HBNBCommand()`, which sub-classes the `cmd.Cmd` class.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """"""
    prompt = "(hbnb)"

    def do_help(self, arg):
        """"""
        return super().do_help(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
