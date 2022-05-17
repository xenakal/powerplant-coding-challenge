import os
from api.production_plan import create_production_plan_app, run_production_plan_app

app, api, socket = create_production_plan_app()
run_production_plan_app(app, api, socket)