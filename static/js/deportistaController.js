(function () {
    'use strict';

    var DeportistaCrtl = function ($rootScope, $scope, $routeParams, $location, deportistaService) {

        var res = deportistaService.list($routeParams.deportistaId).then(function (data) {
            $scope.deportistas = data;
        }, function (response) {
            console.log('Error: ' + response);
        })

        $scope.thumbnail = function (deportistaId) {
            $location.url('/destacado/' + deportistaId);
        };
        $scope.calendario = function (deportistaId) {
            $location.url('/evento/' + deportistaId);
        };
    };

    angular.module('olimpicolombia.controllers').controller('DeportistaCrtl', ['$rootScope', '$scope', '$routeParams', '$location', 'deportistaService', DeportistaCrtl]);
}());