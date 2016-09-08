(function () {
    'use strict';

    var NavCrtl = function ($rootScope, $scope, $location, registrationService) {
        $scope.logout = function () {
            registrationService.logout().then(function (data) {
                    if (data.mensaje == 'ok') {
                        $rootScope.authenticated = false;
                        $location.url("/login");
                    }
                });
        }
    };

    angular.module('olimpicolombia.controllers').controller('navCrtl', ['$rootScope', '$scope', '$location', 'registrationService', NavCrtl]);
}());