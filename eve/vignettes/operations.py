# -*- coding: utf-8 -*-
"""This module contains database operations"""

from rest_framework.exceptions import NotFound

from .models import VignetteType, Vignette

from datetime import datetime, timedelta
from django.utils import timezone


def get_all_vignette_types():
    return [vto for vto in VignetteType.objects.all()]


def get_one_vignette_type(vignette_id):
    try:
        return VignetteType.objects.get(id=vignette_id)
    except VignetteType.DoesNotExist:
        raise NotFound(detail="Vignette Type Not Found")


def get_active_vignette_by_license_plate(license_plate):
    now = timezone.now()
    validVignettes = []

    try:
        for vignette in Vignette.objects.select_related().filter(valid_from__lte=datetime.now()).filter(license_plate=license_plate):
            vignetteType = VignetteType.objects.get(id=vignette.id)
            daysUsed = timedelta(days=(now-vignette.valid_from).days)

            if daysUsed <= vignetteType.duration:
                validVignettes.append(vignette)

        return validVignettes
    except Vignette.DoesNotExist:
        raise NotFound(
            detail={
                "error": "VIGNETTE_NOT_FOUND",
                "message": "Vignette with this license plate doesn't exist.",
                "timestamp": datetime.now()
            }
        )
