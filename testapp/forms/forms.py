from django import forms


class BigForm(forms.Form):
    """
    A form that can test each type of input in the frontend library.
    """

    # input
    national_insurance = forms.CharField(
        label="What is your name?", max_length=7, help_text="Help text"
    )

    # textarea
    more_detail = forms.CharField(
        label="Can you provide more detail?", widget=forms.Textarea
    )

    # radios
    name_changed = forms.ChoiceField(
        choices=[("yes", "Yes"), ("no", "No")],
        label="Have you changed your name?",
        widget=forms.RadioSelect,
    )

    # checkboxes
    nationality = forms.MultipleChoiceField(
        choices=[
            ("british", "British"),
            ("irish", "Irish"),
            ("other", "Citizen of another country"),
        ],
        label="What is your nationality?",
        widget=forms.CheckboxSelectMultiple,
    )

    # select
    select = forms.ChoiceField(
        choices=[
            (None, "-----"),
            ("choice1", "Choice 1"),
            ("choice2", "Choice 2"),
            ("choice3", "Choice 3"),
        ]
    )

    # single checkbox
    confirmation = forms.BooleanField(
        label="Are you sure?",
        help_text="Help text",
    )

    # A hidden field
    hidden = forms.CharField(
        widget=forms.HiddenInput(),
        label="This should never show up",
        help_text="This too",
    )
