import subprocess


class TestGrep():
    def test_grep_data(self):
        """Утилита grep возвращает строку с искомым ключевым словом"""
        command = 'grep linux test.txt'
        result = subprocess.check_output(command, shell=True).decode("utf-8")
        assert result.strip() == 'linux'


    def test_grep_data_2_words(self):
        """Утилита grep возвращает две строки с искомым ключевым словом"""
        command = 'grep testing test.txt'
        result = subprocess.check_output(command, shell=True).decode("utf-8")
        result_formatted = ' '.join(result.splitlines())
        assert result_formatted == 'testing testing'


    def test_get_grep_amount(self):
        """Утилита grep возвращает количество строк, 
        где находится искомое ключевое слово"""
        command = 'grep -c testing test.txt'
        result = subprocess.check_output(command, shell=True).decode("utf-8")
        assert int(result) == 2


    def test_grep_A_flag(self):
        """Утилита grep возвращает две строки, 
        с ключевым словом, и словом находящимся под ключевым"""
        command = 'grep -A 1 pytest test.txt'
        result = subprocess.check_output(command, shell=True).decode("utf-8")
        result_formatted = ''.join(result.splitlines())
        assert result_formatted == 'pytest linux'


    def test_grep_B_flag(self):
        """Утилита grep возвращает две строки, 
        с ключевым словом, и словом находящимся над ключевым"""
        command = 'grep -B 1 pytest test.txt'
        result = subprocess.check_output(command, shell=True).decode("utf-8")
        result_formatted = ' '.join(result.splitlines())
        assert result_formatted.strip() == 'testing pytest'


    def test_grep_C_flag(self):
        """Утилита grep возвращает три строки, 
        с ключевым словом, словом находящимся под ключевым,
        и словом находящимся над ключевым"""
        command = 'grep -C 1 pytest test.txt'
        result = subprocess.check_output(command, shell=True).decode("utf-8")
        result_list = result.splitlines()
        result_formatted = ' '.join([i.strip(' ') for i in result_list])
        assert result_formatted == 'testing pytest linux'