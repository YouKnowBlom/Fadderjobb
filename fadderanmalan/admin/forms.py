from django.forms import ValidationError, ModelForm


class JobAdminForm(ModelForm):
    def clean(self):
        cleaned_data = super(JobAdminForm, self).clean()

        if cleaned_data.get("hidden_until") > cleaned_data.get("hidden_after"):
            raise ValidationError(
                dict(
                    hidden_until="'Hidden until' has to be before 'Hidden after'.",
                    hidden_after="'Hidden until' has to be before 'Hidden after'.",
                )
            )

        if cleaned_data.get("oneway_locked_until") > cleaned_data.get("oneway_locked_after"):
            raise ValidationError(
                dict(
                    oneway_locked_until="'One-way locked until' has to be before 'One-way locked after'.",
                    oneway_locked_after="'One-way locked until' has to be before 'One-way locked after'.",
                )
            )

        if cleaned_data.get("oneway_locked") and cleaned_data.get("locked"):
            raise ValidationError(
                dict(
                    oneway_locked="One-way locked and locked cannot both be enabled.",
                    locked="One-way locked and locked cannot both be enabled.",
                )
            )

        if cleaned_data.get("locked_until") > cleaned_data.get("locked_after"):
            raise ValidationError(
                dict(
                    locked_until="'Locked until' has to be before 'Locked after'.",
                    locked_after="'Locked until' has to be before 'Locked after'.",
                )
            )

        if cleaned_data.get("start_date") == cleaned_data.get("end_date"):
            if cleaned_data.get("start_time") > cleaned_data.get("end_time"):
                raise ValidationError(
                    dict(
                        start_time="'Start time' has to be before 'End time'.",
                        end_time="'Start time' has to be before 'End time'.",
                    )
                )
        elif cleaned_data.get("start_date") > cleaned_data.get("end_date"):
            raise ValidationError(
                dict(
                    start_date="'Start date' has to be before 'End date'.",
                    end_date="'Start date' has to be before 'End date'.",
                )
            )

        return cleaned_data
