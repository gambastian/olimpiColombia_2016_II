(function () {
    'use strict';

    var DeportesCrtl = function ($rootScope, $scope, $location) {

        if ($rootScope.authenticated) {

        } else {
            $location.url("/login");
        }

    };

    angular.module('olimpicolombia.controllers').controller('DeportesCrtl', ['$rootScope', '$scope', '$location', DeportesCrtl]);
}());