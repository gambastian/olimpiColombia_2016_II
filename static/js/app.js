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
        }).otherwise({
            redirectTo: '/deportes'
        });

        // remueve clases css inecesarias
        $compileProvider.debugInfoEnabled(true);

        //Anexa por defecto a todas las llamadas el encabezado
        // $httpProvider.defaults.headers.common["X-Requested-With"] = 'XMLHttpRequest';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    };

    angular.module('olimpicolombia').config(['$routeProvider', '$compileProvider', '$locationProvider', '$httpProvider', Configuration]);
}());