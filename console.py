#!/usr/bin/python3
"""console"""


from models import storage
from models.engine.file_storage import CLASSES

import cmd
import re


class HBNBCommand(cmd.Cmd):
    """This is the main class that will run the application"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """
        Command to handle EOF input, quits the program by default
        """
        self.do_quit(arg)

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        exit(0)

    def do_help(self, arg):
        """Command to list help"""
        return super().do_help(arg)

    def emptyline(self):
        """Does nothing"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg in CLASSES:
            item = CLASSES[arg]()
            item.save()
            print(item.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id
        """
        args = arg.split(' ')
        if not arg:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in CLASSES:
            item_key = '.'.join(args)
            item = storage.all().get(item_key, None)
            if not item:
                print("** no instance found **")
            else:
                print(item)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg, custom_dict=None):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (saves the change into the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Quoted attribute values are treated as strings
        Strings with spaces should be quoted
        """
        args = arg.split(' ', 3)
        all_items = storage.all()
        if not arg:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            item_key = '.'.join(args[:2])
            item = all_items.get(item_key, None)
            if not item:
                print("** no instance found **")
            elif custom_dict:
                new_values = item.to_dict()
                for key, value in custom_dict.items():
                    new_values[key] = value
                all_items[item_key] = CLASSES[args[0]](**new_values)
                all_items[item_key].save()
                return
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                attr_value = args[3]
                if attr_value.isnumeric():
                    if '.' in attr_value:
                        attr_value = float(attr_value)
                    else:
                        attr_value = int(attr_value)
                else:
                    attr_value = args[3].strip('\"\'')
                new_values = all_items[item_key].to_dict()
                new_values[args[2]] = attr_value
                all_items[item_key] = CLASSES[args[0]](**new_values)
                (all_items[item_key]).save()

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        Saves the change into the JSON file
        """
        args = arg.split(' ')
        if not arg:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in CLASSES:
            item_key = '.'.join(args)
            item = storage.all().pop(item_key, None)
            if not item:
                print("** no instance found **")
            else:
                storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split(' ')
        items = storage.all()
        class_type = CLASSES.get(args[0], None)
        if not arg:
            print([str(obj[1]) for obj in items.items()])
        elif class_type:
            objs = [str(obj[1]) for obj in items.items()
                    if type(obj[1]) is class_type]
            print(objs)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        arg_list = line.split('.', 1)
        class_type = CLASSES.get(arg_list[0], None)
        if class_type and len(arg_list) == 2:
            func_call = arg_list[1]
            class_name = arg_list[0]
            items = storage.all()
            objs = [obj[1] for obj in items.items()
                    if type(obj[1]) is class_type]
            if func_call == 'all()':
                print(objs)
                return
            if func_call == 'count()':
                print(len(objs))
                return
            quoted = '\\s*"([^"]+)"\\s*'
            pattern = '^show\\('+quoted+'\\)'
            if re.search(pattern, func_call):
                id = re.findall(quoted, func_call)[0]
                self.do_show(' '.join([class_name, id]))
                return
            pattern = '^destroy\\('+quoted+'\\)'
            if re.search(pattern, func_call):
                id = re.findall(quoted, func_call)[0]
                self.do_destroy(' '.join([class_name, id]))
                return
            string_or_number = '\\s*([^\\s\\)\']+|"[^"]+"|\\d+\\.?\\d+)\\s*'
            pattern = '^update\\('+(quoted+',')*2+string_or_number+'\\)'
            if re.search(pattern, func_call):
                pattern = (quoted + ',')*2 + string_or_number
                args = re.findall(pattern, func_call)[0]
                self.do_update(' '.join([class_name] + args[:3]))
                return
            dict_like = '\\s*(\\{.*\\})\\s*'
            pattern = '^update\\(' + quoted + ',' + dict_like + '\\)'
            if re.search(pattern, func_call):
                pattern = quoted + ',' + dict_like
                args = re.findall(pattern, func_call)[0]
                try:
                    passed_dict = eval(args[1])
                    if not isinstance(passed_dict, dict):
                        raise TypeError()
                    arg = class_name+' '+args[0]
                    self.do_update(arg=arg, custom_dict=passed_dict)
                    return
                except Exception as e:
                    pass
        return super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
