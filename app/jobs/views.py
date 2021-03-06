from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext

from django.contrib import auth
from django.contrib.auth import authenticate, login, views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.core import mail

from django.core.exceptions import ObjectDoesNotExist, ValidationError
import hashlib, datetime, random, math, time, json
from django.utils import timezone
from operator import itemgetter, attrgetter
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from decimal import *
from hashlib import md5
from django.utils.timezone import tzinfo, timedelta, datetime

def register

def sign_in

@login_required
def home_page

@login_required
def employee_profile

@login_required
def company_page

@login_required
def employee_matches

@login_required
def company_matches

@login_required
def get_jobs_by_company

@login_required
def add_new_job

@login_required
def modify_job

@login_required
def log_out


