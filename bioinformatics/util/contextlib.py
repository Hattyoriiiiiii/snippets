import contextlib

@contextlib.contextmanager
def config_test():
    print('start')              # 前処理
    try:
        yield
    finally:
        print('done')           # 後処理

with config_test():
    print('process...')