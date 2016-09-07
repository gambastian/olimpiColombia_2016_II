(function () {
    'use strict';

    var DeportistaSvc = function ($resource, $http) {
        var deportistaService = {
            list: function (deporteId) {
                var promise = $http.get('/api/deportista/' + deporteId, {})
                    .then(function (response) {
                        return response.data;
                    });
                return promise;
            },
            get: function (deportistaId) {
                var promise = $http.get('/api/olimpian/' + deportistaId, {})
                    .then(function (response) {
                        return response.data[0];
                    });
                return promise;
            }
        };

        return deportistaService;
    };

    angular.module('olimpicolombia.services').factory('deportistaService', ['$resource', '$http', DeportistaSvc]);
}());
