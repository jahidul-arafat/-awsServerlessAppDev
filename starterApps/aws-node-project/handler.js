'use strict';

module.exports.hello = async (event,context) => {
  return {
    statusCode: 200,
    body: JSON.stringify(
      {
        messageCore: 'Go Serverless v3.0! Your function executed successfully!',
        myMessage: 'Welcome to jarafatkata.com site launching ceremony!',
        secondMsg: 'Have Patience, Have faith on ALLAH (SWT)',
        eventData: event,
        contextData: context
      },
      null,
      2
    ),
  };
};
