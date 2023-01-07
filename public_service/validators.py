from validate_docbr import CPF


def cpf_valid(number_of_cpf):
    cpf = CPF()
    return cpf.validate(number_of_cpf)


def name_valid(name):
    new_name = name.replace(" ", "")
    return new_name.isalpha()
