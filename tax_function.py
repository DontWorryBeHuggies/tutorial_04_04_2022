import pandas as pd


def evaluates_tax_salary_per_worker(salary: int = 100000) -> pd.DataFrame:
    """
    функция возвращает абсолютное значение налога по каждому взносу от ввндннной зарплаты за 1 месяц

    :param salary: зарплата по которому нужно посчитать налог
    :return: процент налога для уплаты в виде двух столбцов
    """
    ndfl_tax = salary * 0.13
    pfr_tax = salary * 0.22
    med_tax = salary * 0.051
    soc_tax = salary * 0.029
    fcc_tax = salary * 0.02
    tax_sum = sum([ndfl_tax, pfr_tax, med_tax, soc_tax, fcc_tax])
    output_dataframe = pd.DataFrame({'Налон': ['НДФЛ', 'ПФР', 'Медицинское', 'Соц.страх', 'ФСС', 'ИТОГ'],
                                     'Сумма': [ndfl_tax, pfr_tax, med_tax, soc_tax, fcc_tax, tax_sum]})
    return output_dataframe


if __name__ == '__main__':
    print(evaluates_tax_salary_per_worker(265000))
