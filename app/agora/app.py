import os
from dotenv import load_dotenv
import time
from flask import jsonify, request

from . import agora
from .agora_key.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee
from .agora_key.RtmTokenBuilder import RtmTokenBuilder, Role_Rtm_User


@agora.route('/token',  methods=['POST'])
def generate_agora_token():
    userAccount = request.json["email_address"]
    appID = os.getenv('AGORA_APP_ID')
    appCertificate = os.getenv('AGORA_APP_CERTIFICATE')
    expireTimeInSeconds = 3600
    currentTimestamp = int(time.time())
    privilegeExpiredTs = currentTimestamp + expireTimeInSeconds

    if channelName is None:
        return jsonify({"msg": "channelName cannot be null"})

    rtc_token = RtcTokenBuilder.buildTokenWithAccount(
        appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)

    rtm_token = RtmTokenBuilder.buildToken(
        appID, appCertificate, userAccount, Role_Rtm_User, privilegeExpiredTs)
    return jsonify({'token': rtc_token,'rtm_token': rtm_token,'appID': appID, 'channel_name': channelName, 'uid': userAccount})
