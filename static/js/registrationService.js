(function () {
    'use strict';

    var RegistrationSvc = function ($resource, $http) {

        var loginService = {
            login: function (data) {
                //Headers que se deben enviar con la petición
                //X-Requested-With hace que el navegador no muestre un popup alternativo
                var heads = {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/x-www-form-urlencoded',
                };

                var promise = $http.post('/api/login/',
                    {
                        headers: heads,
                        body: data
                    }).then(function (response) {
                    return response.data;
                });
                return promise;
            },
            logout: function () {
                var promise = $http.get('/api/logout', {}).then(function (response) {
                    return response.data;
                });
                return promise;
            },
            islogged: function () {
                var promise = $http.get('/api/islogged', {}).then(function (response) {
                    return response.data;
                });
                return promise;
            }
        };

        return loginService;

    };

    angular.module('olimpicolombia.services').factory('registrationService', ['$resource', '$http', RegistrationSvc]);
}());
