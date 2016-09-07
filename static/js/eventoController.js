(function () {
    'use strict';

    var EventoCrtl = function ($rootScope, $scope, $routeParams, eventoService, deportistaService, deportesService) {

        var res = eventoService.list($routeParams.deportistaId).then(function (data) {
            $scope.eventos = data;
            var dep = deportistaService.get($routeParams.deportistaId).then(function (deportista) {
                console.log(JSON.stringify(deportista));
                $scope.deportista = deportista;
            })
        }, function (response) {
            console.log('Error: ' + response);
        })
    };

    angular.module('olimpicolombia.controllers').controller('eventoCrtl', ['$rootScope', '$scope', '$routeParams', 'eventoService', 'deportistaService', 'deportesService', EventoCrtl]);
}());