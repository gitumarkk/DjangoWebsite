def dynamic_menu(request):
    # Adds Dynamic Menu Template Context
    from models import Registration
    try:
        Registration.objects.get(pk=1)
        return{"registration_open": True}
    except Registration.DoesNotExist:
        return {"registration_open": False}
