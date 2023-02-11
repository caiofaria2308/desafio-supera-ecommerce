
def test_new_user_incorrect_cpf(db, user):
    incorrect_cpf = "173.081.550-20"
    user.cpf = incorrect_cpf
    try:
        user.save()
        assert False
    except:
        assert True
    