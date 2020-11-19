def type_textfield(webelement, text, clear_field=True):
    if clear_field:
        webelement.clear()
    webelement.send_keys(text)
