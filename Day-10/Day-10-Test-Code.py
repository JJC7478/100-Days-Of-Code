from pkg_resources import fixup_namespace_packages

#Functions with Outputs
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name(input("What is your first name?"), input("What is your last name?"))
print(formatted_string)