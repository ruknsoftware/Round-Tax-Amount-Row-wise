app_name = "round_tax_amount_row_wise"
app_title = "Round Tax Amount Row Wise"
app_publisher = "Hamza Abuabada"
app_description = "Round Tax Amount Row Wise"
app_email = "abadahhamza@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/round_tax_amount_row_wise/css/round_tax_amount_row_wise.css"
# app_include_js = "/assets/round_tax_amount_row_wise/js/round_tax_amount_row_wise.js"

# include js, css files in header of web template
# web_include_css = "/assets/round_tax_amount_row_wise/css/round_tax_amount_row_wise.css"
# web_include_js = "/assets/round_tax_amount_row_wise/js/round_tax_amount_row_wise.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "round_tax_amount_row_wise/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "round_tax_amount_row_wise.utils.jinja_methods",
# 	"filters": "round_tax_amount_row_wise.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "round_tax_amount_row_wise.install.before_install"
# after_install = "round_tax_amount_row_wise.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "round_tax_amount_row_wise.uninstall.before_uninstall"
# after_uninstall = "round_tax_amount_row_wise.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "round_tax_amount_row_wise.utils.before_app_install"
# after_app_install = "round_tax_amount_row_wise.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "round_tax_amount_row_wise.utils.before_app_uninstall"
# after_app_uninstall = "round_tax_amount_row_wise.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "round_tax_amount_row_wise.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"round_tax_amount_row_wise.tasks.all"
# 	],
# 	"daily": [
# 		"round_tax_amount_row_wise.tasks.daily"
# 	],
# 	"hourly": [
# 		"round_tax_amount_row_wise.tasks.hourly"
# 	],
# 	"weekly": [
# 		"round_tax_amount_row_wise.tasks.weekly"
# 	],
# 	"monthly": [
# 		"round_tax_amount_row_wise.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "round_tax_amount_row_wise.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "round_tax_amount_row_wise.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "round_tax_amount_row_wise.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["round_tax_amount_row_wise.utils.before_request"]
# after_request = ["round_tax_amount_row_wise.utils.after_request"]

# Job Events
# ----------
# before_job = ["round_tax_amount_row_wise.utils.before_job"]
# after_job = ["round_tax_amount_row_wise.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"round_tax_amount_row_wise.auth.validate"
# ]
