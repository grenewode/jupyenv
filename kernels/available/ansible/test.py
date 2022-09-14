import os
from testbook import testbook

current_dir = os.path.dirname(os.path.abspath(__file__))

@testbook(f'{current_dir}/test.ipynb', execute=True, kernel_name="example_ansible")
def test_nb(tb):
    result = tb.cell_output_text(0)
    print("Output:")
    print(result)
    assert "ERROR" not in result

if __name__ == '__main__':
    test_nb()
