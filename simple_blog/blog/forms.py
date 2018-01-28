from django import forms


class EmailPostForm(forms.Form):
	first_name = forms.CharField(
		max_length=25
		)
	surname = forms.CharField(
		max_length=25
		)
	email = forms.EmailField(
		)
	to = forms.EmailField(
		)
	comments = forms.CharField(
		required=False, 
		widget=forms.Textarea
		)