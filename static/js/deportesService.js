(function () {
    'use strict';

    var DeportesSvc = function ($resource, $http) {

        var deportesService = {
            list: function () {
                var promise = $http.get('/api/deportes/', {})
                    .then(function (response) {
                        return response.data;
                    });
                return promise;
            }
        };

        return deportesService;
    };

    angular.module('olimpicolombia.services').factory('deportesService', ['$resource', '$http', DeportesSvc]);
}());
