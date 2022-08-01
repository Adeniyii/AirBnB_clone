# Building the console
Scrapbook to organize thoughts as we build out the AirBnB command line interpreteter.

## [cmd](https://docs.python.org/3.8/library/cmd.html#module-cmd) — Support for line-oriented command interpreters

The `Cmd` class provides a simple framework for writing line-oriented command interpreters. These are often useful for test harnesses, administrative tools, and prototypes that will later be wrapped in a more sophisticated interface.

A `Cmd` instance or subclass instance is a line-oriented interpreter framework. There is no good reason to instantiate `Cmd` itself; rather, it’s useful as a superclass of an interpreter class you define yourself in order to inherit `Cmd`’s methods and encapsulate action methods.

## Important concepts 🎓
- Cmd.cmdloop(intro=None)
  - Repeatedly issue a prompt, accept input, parse an initial prefix off the received input, and dispatch to action methods, passing them the remainder of the line as argument.
  - All subclasses of `Cmd` inherit a predefined `do_help()`. This method, called with an argument 'bar', invokes the corresponding method `help_bar()`, and if that is not present, prints the docstring of `do_bar()`, if available. With no argument, `do_help()` lists all available help topics (that is, all commands with corresponding `help_*()` methods or commands that have docstrings), and also lists any undocumented commands.
  - This method will return when the `postcmd()` method returns a `true` value. The stop argument to `postcmd()` is the return value from the command’s corresponding `do_*()` method.
- An end-of-file on input is passed back as the string 'EOF'.
- An interpreter instance will recognize a command name `foo` if and only if it has a method `do_foo()`. As a special case, a line beginning with the character '?' is dispatched to the method `do_help()`. As another special case, a line beginning with the character '!' is dispatched to the method `do_shell()` (if such a method is defined).
- Implement `do_EOF()` to gracefully catch errors.
- Implement `emptyline()` to override default `empty line + return` behaviour.
