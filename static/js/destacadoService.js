(function () {
    'use strict';

    var DestacadoSvc = function ($http) {

        var destacadoService = {
            list: function (deportistaId) {
                var promise = $http.get('/api/destacado/' + deportistaId, {})
                    .then(function (response) {
                        return response.data;
                    });
                return promise;
            }
        };

        return destacadoService;
    };

    angular.module('olimpicolombia.services').factory('destacadoService', ['$http', DestacadoSvc]);
}());
