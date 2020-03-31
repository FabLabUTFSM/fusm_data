from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import ExtendedDefaultRouter
from .views import (
    PersonaViewSet, 
    PerfilProfesionalViewSet,
    PerfilUSMViewSet,
    TipoActividadViewSet,
    TipoCampusViewSet,
    TipoCarreraViewSet,
    TipoGeneroViewSet,
    TipoUnidadViewSet
)

router = ExtendedDefaultRouter()

router.register('personas', PersonaViewSet)
router.register('profesionales', PerfilProfesionalViewSet)
router.register('usm', PerfilUSMViewSet)

router.register('tipos/actividades', TipoActividadViewSet)
router.register('tipos/campus', TipoCampusViewSet)
router.register('tipos/carreras', TipoCarreraViewSet)
router.register('tipos/generos', TipoGeneroViewSet)
router.register('tipos/unidades', TipoUnidadViewSet)
