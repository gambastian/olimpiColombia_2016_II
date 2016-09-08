(function () {
    'use strict';

    var CrearUsuarioCrtl = function ($rootScope, $scope, $location, crearUsuarioService) {

        $scope.error = false;
        $scope.create = function () {
            if ($scope.form.password.length >= 8) {
                var res = crearUsuarioService.create($scope.form).then(function (data) {
                    console.log(JSON.stringify(data));
                    if (data.mensaje == 'ok') {
                        $location.url("/deportes");
                    } else {
                        console.log('Ocurrio un error:' + data);
                        $scope.error = true;
                        $scope.mensaje = data.mensaje;
                    }
                })
            } else {
                $scope.error = true;
                $scope.mensaje = 'La clave debe ser mayor a 8 caracteres y debe tener numeros y letras';
            }
        }
    };

    angular.module('olimpicolombia.controllers').controller('crearUsuarioCrtl', ['$rootScope', '$scope', '$location', 'crearUsuarioService', CrearUsuarioCrtl]);
}());