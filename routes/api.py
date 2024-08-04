""" Here we define the routes for the HTTP server. """
from core.facades.http import Router
from app.controllers.api import ApiController

Router.get("/ping", ApiController, "ping")

# URL routes
Router.post("/url", ApiController, "create_url")
Router.get("/url/{short_url}", ApiController, "get_url")
Router.get("/stats", ApiController, "get_general_stats")
Router.delete("/url/{short_url}", ApiController, "delete_url")
Router.get("/url/{short_url}/stats", ApiController, "get_url_stats")
Router.get("/{short_url}", ApiController, "redirect_url")
