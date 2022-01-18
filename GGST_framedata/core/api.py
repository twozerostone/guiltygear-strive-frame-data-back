from ninja import NinjaAPI
from .frame.api import router as frame_router

api_v1 = NinjaAPI(version='1.0.0')

api_v1.add_router("/frame/", frame_router)
