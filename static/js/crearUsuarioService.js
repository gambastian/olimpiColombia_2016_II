(function () {
        'use strict';

        var CrearUsuarioSvc = function ($http) {
            var loginService = {
                create: function (data) {
                    var heads = {
                        'X-Requested-With': 'XMLHttpRequest',
                        'Content-Type': 'application/x-www-form-urlencoded',
                    };

                    var promise = $http.post('/api/crear_usuario',
                        {
                            headers: heads,
                            body: data
                        }).then(function (response) {
                        return response.data;
                    });
                    return promise;
                }
            };

            return loginService;
        };

        angular.module('olimpicolombia.services').factory('crearUsuarioService', ['$http', CrearUsuarioSvc]);
    }()
);
