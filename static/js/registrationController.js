(function () {
    'use strict';

    var RegistrationCrtl = function ($rootScope, $scope) {
        $scope.error = false;
        $scope.submitForm = function () {
            console.log("entra en la funcion");

            $scope.error = !$scope.error;
        }

    };

    angular.module('olimpicolombia.controllers').controller('RegistrationCrtl', ['$rootScope', '$scope', RegistrationCrtl]);
}());