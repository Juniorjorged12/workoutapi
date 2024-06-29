run:
	@uvicorn workout_api.main:app --reload

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)


run_migations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head