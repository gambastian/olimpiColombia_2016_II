(function () {
    'use strict';

    var DestacadoCtrl = function ($rootScope, $scope, $routeParams, destacadoService) {

        var res = destacadoService.list($routeParams.deportistaId).then(function (data) {
            console.log(JSON.stringify(data[0].fields.video));
            $scope.video = data[0].fields.video;
        }, function (response) {
            console.log('Error: ' + response);
        })
    };

    angular.module('olimpicolombia.controllers').controller('destacadoCtrl', ['$rootScope', '$scope', '$routeParams', 'destacadoService', DestacadoCtrl]);
}());