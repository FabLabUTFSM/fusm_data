from rest_framework.routers import DefaultRouter
from .views import (
    ClaseMaquinaViewSet,
    MaquinaViewSet,
    TareaMantenimientoViewSet,
    MantenimientoViewSet,
    TipoClasificacionViewSet
)


router = DefaultRouter()
router.register('clases_maquina', ClaseMaquinaViewSet)
router.register('maquinas', MaquinaViewSet)
router.register('tareas_mantenimiento', TareaMantenimientoViewSet)
router.register('mantenimientos', MantenimientoViewSet)
router.register('tipos/clasificaciones', TipoClasificacionViewSet)