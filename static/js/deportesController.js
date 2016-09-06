(function () {
    'use strict';

    var DeportesCrtl = function ($rootScope, $scope, $location, deportesService) {
        if ($rootScope.authenticated) {
            // $scope.deportes=;

            var res = deportesService.list().then(function (data) {
                console.log('OK: ' + JSON.stringify(data));
                $scope.deportes=data;
            }, function (response) {
                $scope.error = true;
                console.log('Error: ' + response);
            })

        } else {
            $location.url("/login");
        }
    };

    angular.module('olimpicolombia.controllers').controller('DeportesCrtl', ['$rootScope', '$scope', '$location', 'deportesService', DeportesCrtl]);
}());