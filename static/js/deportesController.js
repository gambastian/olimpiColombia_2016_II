(function () {
    'use strict';

    var DeportesCrtl = function ($rootScope, $scope, $location, deportesService) {
        if ($rootScope.authenticated) {

            var res = deportesService.list().then(function (data) {
                $scope.deportes = data;
            }, function (response) {
                $scope.error = true;
                console.log('Error: ' + response);
            })

        } else {
            $location.url("/login");
        }

        $scope.deportistas = function (id) {
            $location.url("/deportista/" + id);
        }
    };

    angular.module('olimpicolombia.controllers').controller('DeportesCrtl', ['$rootScope', '$scope', '$location', 'deportesService', DeportesCrtl]);
}());