str1 = input()

if ((('лилипут' in str1) or ('Лилипут' in str1) or ('ЛИЛИПУТ' in str1)) and
        (('великан' in str1) or ('Великан' in str1) or ('ВЕЛИКАН' in str1))):
    print('Я совсем запутался.')
elif ('великан' in str1) or ('Великан' in str1) or ('ВЕЛИКАН' in str1):
    print('В Великании.')
elif ('лилипут' in str1) or ('Лилипут' in str1) or ('ЛИЛИПУТ' in str1):
    print('В Лилипутии.')
else:
    print('Я совсем запутался.')