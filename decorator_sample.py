# 関数a
def a():
    print('Aです')

# 関数b
def b(func):
    print('===開始===')
    func()
    print('===終了===')

# 関数の実行
b(a)