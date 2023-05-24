from var_11 import var11


def test_var11_alive():
    data = ['0,1,2,3,4,5,6,7,8,9,20,1', '0,0,2,3,4,5,6,7,8,9,10,1', '0,0,2,3,4,5,6,7,8,9,20,1',
            '0,1,4,8,9,15,46,3,5,2,20,1', '0,0,0,3,4,5,6,7,8,9,30,1', '0,1,72,36,41,50,62,70,89,20,20,1']
    assert var11(data, '1') == 20


def test_var11_dead():
    data = ['0,1,2,3,4,5,6,7,8,9,20,1', '0,0,2,3,4,5,6,7,8,9,10,1', '0,0,2,3,4,5,6,7,8,9,20,1',
            '0,1,4,8,9,15,46,3,5,2,20,1', '0,0,0,3,4,5,6,7,8,9,60,1', '0,1,72,36,41,50,62,70,89,20,20,1']
    assert var11(data, '0') == 30
