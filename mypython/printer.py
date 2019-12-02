def pr_str(mal_type):
    if type(mal_type) == list:
        return "(" + " ".join([pr_str(mt) for mt in mal_type]) + ")"
    return str(mal_type)