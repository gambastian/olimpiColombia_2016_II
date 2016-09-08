/**
 * @name olimpicolombia
 * @description Aplicacion principal
 */
(function () {
    'use strict';

    var olimpicolombia = angular.module('olimpicolombia', ['ngCookies', 'ngRoute', 'ngResource', 'olimpicolombia.controllers', 'olimpicolombia.services']);
    var olimpicolombiaControllers = angular.module('olimpicolombia.controllers', []);
    var olimpicolombiaServices = angular.module('olimpicolombia.services', []);

    var Configuration = function ($routeProvider, $compileProvider, $locationProvider, $httpProvider) {
        $routeProvider.when('/deportes', {
            templateUrl: 'static/partials/deportes.html',
            controller: 'DeportesCrtl'
        }).when('/login', {
            templateUrl: 'static/partials/login.html',
        }).when('/registro', {
            templateUrl: 'static/partials/registration_form.html',
            controller: 'RegistrationCrtl'
        }).when('/deportista/:deportistaId', {
            templateUrl: 'static/partials/deportista.html',
            controller: 'DeportistaCrtl'
        }).when('/destacado/:deportistaId', {
            templateUrl: 'static/partials/destacado.html',
            controller: 'destacadoCtrl'
        }).when('/evento/:deportistaId', {
            templateUrl: 'static/partials/evento.html',
            controller: 'eventoCrtl'
        }).when('/crear_usuario', {
            templateUrl: 'static/partials/crearUsuario.html',
            controller: 'crearUsuarioCrtl'
        }).otherwise({
            redirectTo: '/deportes'
        });

        // remueve clases css inecesarias
        $compileProvider.debugInfoEnabled(true);

        //Anexa por defecto a todas las llamadas el encabezado
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    };

    angular.module('olimpicolombia').config(['$routeProvider', '$compileProvider', '$locationProvider', '$httpProvider', Configuration]);
}());