from time import sleep

from xmlinport.views import *
from xmlinport.models import *


def update_products_xml(json_datafile):
    global envelope, envelopefor
    data_json = json_datafile
    trades_list = list()
    trade_places_inn = list()
    # trade_place = TradePlace()
    # trade_place_list = TradePlaceList()
    # trade_place_list.trade_place = trade_place
    # trade_list = TradeList()

    # trade_place.save()
    # trade_place_list.save()
    # trade_place_list = TradePlaceList()

    for i in range(len(data_json["TradePlaceList"]["TradePlace"])):
        for tradelists in data_json["TradePlaceList"]["TradePlace"][i]["TradeList"]:
            trades_list.append(tradelists)
            inn = data_json["TradePlaceList"]["TradePlace"][i]["@INN"]
            trade_places_inn.append(inn)

    #print(len(trade_places_inn))
    #print(len(trades_list), "))))))))))))))")
    # sleep(30)
    j = 0
    for trade in trades_list:

        try:
            if type({}) == type(trade["Trade"]["Message"]):
                bidding_fail = BiddingFail()  # BiddingFail
                bidding_proccess_info = BiddingProcessInfo()
                bidding_cancel = BiddingCancel()
                bidding_end = BiddingEnd()
                contract_sale = ContractSale()
                set_contract_sale = SetContractSale()
                bidding_start = BiddingStart()
                bidding_pause = BiddingPause()
                application_session_start = ApplicationSessionStart()
                application_session_end = ApplicationSessionEnd()
                bidding_result = BiddingResult()
                price_info = PriceInfo()
                application_session_statistic = ApplicationSessionStatistic()
                lot_statistic = LotStatistic()
                lot_trade_result = LotTradeResult()
                success_trade_result = SuccessTradeResult()
                bidding_state_lot_info = BiddingStateLotInfo()
                attach = Attach()

                winner_person = WinnerPerson()
                winner_company = WinnerCompany()
                debtor_person = DeptorPerson()
                debtor_company = DebtorCompany()
                bidding_invitation = BiddingInvitation()
                legal_case = LegalCase()
                arbitr_manager = ArbitrManager()
                trade_organizer_person = TradeOrganizerPerson()
                trade_organizer_company = TradeOrganizerCompany()
                trade_info = TradeInfo()
                open_form = OpenForm()
                close_form = CloseForm()
                application = Application()
                lot = Lot()
                lot_list = LotList()
                classificaition = Classification()
                participant_person = ParticipantPerson()
                lot_info = LotInfo()
                failure_trade_result = FailureTradeResult()
                application_dataa = ApplicationData()
                message_model = Message()
                application_list = ApplicationList()
                trade_model = Trade()
                trade_list = TradeList()
                trade_place = TradePlace()
                trade_place_list = TradePlaceList()
                envelope_model = Envelope()
                body = Body()
                set_application_session_statistic = SetApplicationSessionStatistic()
                set_application_session_end = SetApplicationSessionEnd()
                set_application_session_start = SetApplicationSessionStart()
                set_bidding_end = SetBiddingEnd()
                set_bidding_start = SetBiddingStart()
                set_bidding_fail = SetBiddingFail()
                set_bidding_resume = SetBiddingResume()
                set_bidding_cancel = SetBiddingCancel()
                lot_contract_sale = LotContractSale()
                lot_contract_sale_list = LotContractSaleList()
                contract_info = ContractInfo()
                contract_participant_list = ContractParticipantList()
                contract_participant = ContractParticipant()
                # contract_number_model = ContractNumber()
                trade_organizer = TradeOrganizer()
                set_bidding_result = SetBiddingResult()
                set_bidding_invitation = SetBiddingInvitation()
                debtor = Debtor()

                try:
                    id_efrsb = trade["Trade"]["@ID_EFRSB"]
                    #print(id_efrsb)
                    trade_model.id_efrsb = id_efrsb
                except:
                    pass
                Id = trade["Trade"]["Message"]["@ID"]  # Message ID
                #print(Id)
                # sleep(20)

                try:
                    id_external = trade["Trade"]["@ID_EXTERNAL"]
                    trade_model.id_external = id_external
                    #print(id_external)
                except:
                    pass
                # #print(trades_list)
                #print(type(trades_list))
                Id = trade["Trade"]["Message"]["@ID"]  # Message ID
                try:
                    envelop = trade["Trade"]["Message"]["soap:Envelope"]["soap:Body"]
                    envelope = envelop
                except:
                    pass
                try:
                    envelop = trade["Trade"]["Message"]["SOAP-ENV:Envelope"]["SOAP-ENV:Body"]
                    envelope = envelop
                except:
                    pass
                try:
                    envelop = trade["Trade"]["Message"]["S:Envelope"]["S:Body"]
                    envelope = envelop
                except:
                    pass
                try:
                    envelop = trade["Trade"]["Message"]["soapenv:Envelope"]["soapenv:Body"]
                    envelope = envelop
                except:
                    pass
                try:
                    envelop = trade["Trade"]["Message"]["soapenv:Envelope"]["soapenv:Body"]
                    envelope = envelop
                except:
                    pass
                try:
                    envelop = trade["Trade"]["Message"]["soap:Envelope"]["soap:Body"]
                    envelope = envelop
                except:
                    pass

                try:
                    envelop = trade["Trade"]["Message"]["S:Envelope"]["S:Body"]
                    envelope = envelop
                except:
                    pass

                try:

                    envelop = trade["Trade"]["Message"]["SOAP-ENV:Envelope"]["SOAP-ENV:Body"]
                    envelope = envelop
                except:
                    pass
                try:
                    envelop = trade["Trade"]["Message"]["s:Envelope"]["s:Body"]
                    envelope = envelop
                except:
                    pass
                try:
                    envelop = trade["Trade"]["Message"]["soapenv:Envelope"]["soapenv:Body"]
                    envelope = envelop
                except:
                    pass
                try:
                    envelop = trade["Trade"]["Message"]["soapenv:Envelope"]["soapenv:Body"]
                    envelope = envelop
                except:
                    pass

                # Содержимое Envelope ниже
                try:
                    message_id = trade["Trade"]["Message"]["@ID"]
                    # trade_model.
                    #print(message_id)
                except:
                    pass
                try:
                    xmlns_xsi = envelope["@xmlns:xsi"]
                    #print("xmlns_xsi", xmlns_xsi)
                except:
                    pass
                try:
                    xmlns_xsd = envelope["@xmlns:xsd"]
                    #print("xmlns_xsd", xmlns_xsd)
                except:
                    pass
                try:
                    xmlns_soap = envelope["@xmlns:soap"]
                    #print("xmlns_soap", xmlns_soap)
                except:
                    pass
                # Содержимое SetApplicationSessionStatistic ниже
                try:
                    xmlns = envelope["SetApplicationSessionStatistic"]["@xmlns"]
                    #print("xmlns", xmlns)
                except:
                    pass
                try:
                    xmlns = envelope["SetBiddingFail"]["@xmlns"]
                    #print("xmlns", xmlns)
                except:
                    pass
                # SetBiddingProcessInfo
                try:
                    xmlns = envelope["SetBiddingProcessInfo"]["@xmlns"]
                    #print("xmlns", xmlns)
                except:
                    pass
                # Содержимое ApplicationSessionStatistic ниже
                try:
                    trade_id = envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                        "@TradeId"]
                    application_session_statistic.trade_id = trade_id
                    #print('TradeID', trade_id)
                    trades_list.trade_id = trade_model

                except:
                    pass

                try:
                    trade_id = envelope["SetBiddingFail"]["BiddingFail"][
                        "@TradeId"]

                    bidding_fail.trade_id = trade_id
                    trades_list.trade_id = trade_model
                    #print("TradeId", trade_id)
                except:
                    pass
                try:
                    trade_id = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"][
                        "@TradeId"]
                    bidding_proccess_info.trade_id = trade_id
                    trades_list.trade_id = trade_model
                    #print("TradeId", trade_id)
                except:
                    print("Some error")
                try:
                    trade_id = envelope["SetApplicationSessionStart"]["ApplicationSessionStart"][
                        "@TradeId"]
                    application_session_start.trade_id = trade_id
                    trades_list.trade_id = trade_model
                    #print("TradeId", trade_id)
                except:
                    pass
                try:
                    trade_id = envelope["SetBiddingResult"]["BiddingResult"][
                        "@TradeId"]
                    bidding_result.trade_id = trade_id
                    # trades_list.trade_id = trade_model
                    #print("TradeId", trade_id)
                except:
                    pass
                try:
                    substantiation = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"][
                            "FailureTradeResult"]["Substantiation"]
                    failure_trade_result.substantiation = substantiation

                    #print("substantiation", substantiation)
                except:
                    pass
                try:
                    price = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"][
                            "FailureTradeResult"]["Price"]
                    failure_trade_result.price = price

                    #print("price", price)
                except:
                    pass
                try:
                    trade_id = envelope["SetBiddingCancel"]["BiddingCancel"][
                        "@TradeId"]
                    bidding_cancel.trade_id = trade_id
                    # trades_list.trade_id = trade_model
                    #print("TradeId", trade_id)
                except:
                    pass
                try:
                    trade_id = envelope["SetContractSale"]["ContractSale"][
                        "@TradeId"]
                    contract_sale.trade_id = trade_id
                    # trades_list.trade_id = trade_model
                    #print("TradeId", trade_id)
                except:
                    pass

                try:
                    event_time = envelope["SetContractSale"]["ContractSale"][
                        "@EventTime"]
                    contract_sale.event_time = event_time
                    #print("EventTime", event_time)
                except:
                    pass
                try:
                    lot_number = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "@LotNumber"]
                    lot_contract_sale.lot_number = lot_number
                    #print("LotNumber", lot_number)
                except:
                    pass
                # #winnerCompany
                # try:
                #     full_name = \
                #         envelope["SetBiddingResult"]["BiddingResult"][
                #             "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                #             "WinnerCompany"]["@FullName"]
                #     winner_company.full_name= full_name
                #     #print("FullName", full_name)
                # except:
                #     pass
                #
                # try:
                #     short_name = \
                #         envelope["SetBiddingResult"]["BiddingResult"][
                #             "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                #             "WinnerCompany"]["@ShortName"]
                #     winner_company.short_name = short_name
                #     #print("ShortName", short_name)
                # except:
                #     pass
                # try:
                #     inn = \
                #         envelope["SetBiddingResult"]["BiddingResult"][
                #             "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                #             "WinnerCompany"]["@INN"]
                #     winner_company.inn= inn
                #     #print("INN", inn)
                # except:
                #     pass
                # try:
                #     ogrn = \
                #         envelope["SetBiddingResult"]["BiddingResult"][
                #             "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                #             "WinnerCompany"]["@OGRN"]
                #     winner_company.ogrn= ogrn
                #     #print("OGRN", ogrn)
                # except:
                #     pass
                # try:
                #     legal_address = \
                #         envelope["SetBiddingResult"]["BiddingResult"][
                #             "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                #             "WinnerCompany"]["@LegalAddress"]
                #     winner_company.legal_address = legal_address
                #     #print("Address", address)
                # except:
                #     pass
                # #WinnerCompanyEnd
                try:
                    contract_number = \
                        envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                            "ContractInfo"][
                            "ContractNumber"]
                    contract_info.contract_number = contract_number
                    #print("ContractNumber", contract_number)
                except:
                    pass
                try:
                    date_contract = \
                        envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                            "ContractInfo"][
                            "DateContract"]
                    contract_info.date_contract = date_contract
                    #print("DateContract", date_contract)
                except:
                    pass

                try:
                    price = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "ContractInfo"][
                        "Price"]
                    contract_info.price = price
                    #print("Price", price)
                except:
                    pass
                try:
                    name = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "ContractParticipantList"][
                        "ContractParticipant"]["@Name"]
                    contract_participant.name = name
                    #print("Name", name)
                except:
                    pass
                try:
                    inn = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "ContractParticipantList"][
                        "ContractParticipant"]["@INN"]
                    contract_participant.inn = inn
                    #print("inn", inn)
                except:
                    pass
                try:
                    ogrn = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "ContractParticipantList"][
                        "ContractParticipant"]["@OGRN"]
                    contract_participant.ogrn = ogrn
                    #print("OGRN", ogrn)
                except:
                    pass
                try:
                    is_winner = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "ContractParticipantList"][
                        "ContractParticipant"]["@IsWinner"]
                    # contract_participant.is_winner = is_winner
                    contract_participant.is_winner = json.loads(is_winner)

                    #print("IsWinner", is_winner)
                except:
                    pass
                try:
                    is_buyer = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "ContractParticipantList"][
                        "ContractParticipant"]["@IsBuyer"]
                    # contract_participant.is_buyer = is_buyer
                    contract_participant.is_buyer = json.loads(is_buyer)

                    #print("IsBuyer", is_buyer)
                except:
                    pass
                # ++++++---------------------------------------------------------------
                try:
                    event_time = envelope["SetApplicationSessionStart"]["ApplicationSessionStart"][
                        "@EventTime"]
                    application_session_start.event_time = event_time
                    #print("EventTime", event_time)
                except:
                    pass
                try:
                    event_time = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"][
                        "@EventTime"]
                    bidding_proccess_info.event_time = event_time
                    #print("EventTime", event_time)
                except:
                    pass
                try:
                    event_time = envelope["SetBiddingResult"]["BiddingResult"][
                        "@EventTime"]
                    bidding_result.event_time = event_time
                    #print("EventTime", event_time)
                except:
                    pass
                try:
                    lot_number = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"][
                        "PriceInfo"]["@LotNumber"]
                    price_info.lot_number = lot_number
                    #print("LotNumber", lot_number)
                except:
                    pass
                try:
                    lot_number = envelope["SetApplicationSessionStart"]["ApplicationSessionStart"][
                        "LotList"]["LotInfo"]["@LotNumber"]
                    price_info.lot_number = lot_number
                    #print("LotNumber", lot_number)
                except:
                    pass
                try:
                    new_price = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"][
                        "PriceInfo"]["@NewPrice"]
                    price_info.new_price = new_price
                    #print("NewPrice", new_price)
                except:
                    pass
                try:
                    event_time = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"][
                        "@EventTime"]
                    application_session_statistic.event_time = event_time
                    #print('EventTime', event_time)

                except:
                    pass
                try:
                    event_time = envelope["SetBiddingFail"]["BiddingFail"][
                        "@EventTime"]
                    bidding_fail.event_time = event_time
                    #print('EventTime', event_time)

                except:
                    pass
                try:
                    event_time = envelope["SetBiddingCancel"]["BiddingCancel"][
                        "@EventTime"]
                    bidding_cancel.event_time = event_time
                    #print('EventTime', event_time)

                except:
                    pass
                try:
                    date_begin = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"][
                        "DateBegin"]
                    application_session_statistic.date_begin = date_begin
                    #print("DateBegin", date_begin)

                except:
                    pass
                    # Содержимое LostLit/LotStatistic ниже
                try:
                    lot_number = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["@LotNumber"]
                    lot_statistic.lot_number = lot_number
                    #print("LotNumber", lot_number)

                except:
                    pass
                try:
                    lot_number = envelope["SetBiddingResult"][
                        "BiddingResult"]["LotList"]["LotTradeResult"]["@LotNumber"]
                    lot_trade_result.lot_number = lot_number
                    #print("LotNumber", lot_number)

                except:
                    pass

                try:
                    lot_number = envelope["SetBiddingFail"]["BiddingFail"][
                        "LotList"]["BiddingStateLotInfo"]["@LotNumber"]
                    #print("LotNumber", lot_number)
                    bidding_state_lot_info.lot_number = lot_number

                except:
                    pass
                try:
                    reason = envelope["SetBiddingFail"]["BiddingFail"][
                        "LotList"]["BiddingStateLotInfo"]["@Reason"]
                    #print("Reason", reason)
                    bidding_state_lot_info.reason = reason

                except:
                    pass
                try:
                    reason = envelope["SetBiddingCancel"]["BiddingCancel"]["@Reason"]
                    #print("Reason", reason)
                    bidding_cancel.reason = reason

                except:
                    pass
                try:
                    reason = envelope["SetBiddingFail"]["BiddingFail"]["@Reason"]
                    #print("Reason", reason)
                    bidding_fail.reason = reason

                except:
                    pass
                try:
                    reason = envelope["SetBiddingFail"]["BiddingFail"]["LotList"]["BiddingStateLotInfo"]["@Reason"]
                    # print("Reason", reason)
                    bidding_fail.reason = reason

                except:
                    pass
                try:
                    reason = envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                        "LotList"]["BiddingStateLotInfo"]["@Reason"]
                    bidding_state_lot_info.reason = reason
                    #print("Reason", reason)

                except:
                    pass
                try:
                    accept_count = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["@AcceptCount"]
                    lot_statistic.accept_count = accept_count
                    #print("AcceptCount", accept_count)

                except:
                    pass
                try:
                    entry_count = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["@EntryCount"]
                    lot_statistic.entry_count = entry_count
                    #print("EntryCount", entry_count)
                    # "@EntryCount"
                except:
                    pass

                try:
                    result = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["ApplicationList"]["ApplicationData"][
                        "@Result"]
                    application_dataa.result = result
                    #print("result", result)

                except:
                    pass
                # try:
                #     result = envelope["SetApplicationSessionStatistic"][
                #         "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["ApplicationList"]["ApplicationData"]
                #     for i in range(len(result)):
                #         #print(i)
                #         sleep(2)
                #         res = result[i]
                #         #print(res)
                #         sleep(2)
                #         result = res["@Result"]
                #         #print(result)
                #         sleep(2)
                #         application_dataa.result = result
                #         application_dataa.save()
                #     #print("result", result)
                #
                # except:
                #     pass
                try:
                    cause_of_refuse = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["ApplicationList"]["ApplicationData"][
                        "@CauseOfRefuse"]
                    application_dataa.cause_of_refuse = cause_of_refuse
                    #print("CauseOfRefuse", cause_of_refuse)

                except:
                    pass
                try:
                    cause_of_refuse = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["ApplicationList"]["ApplicationData"][
                        "@CauseOfRefuse"]
                    application_dataa.cause_of_refuse = cause_of_refuse
                    #print("CauseOfRefuse", cause_of_refuse)

                except:
                    pass

                # Содержимое Attach ниже
                try:
                    filename = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["Attach"]["FileName"]
                    attach.file_name = filename
                    #print("FileName", filename)

                except:
                    pass
                try:
                    Type = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["Attach"]["Type"]
                    attach.type = Type
                except:
                    pass
                try:
                    Blob = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["Attach"]["Blob"]
                    attach.blob = Blob
                except:
                    pass
                # WinnerPerson
                try:
                    first_name = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@FirstName"]
                    winner_person.first_name = first_name
                    #print("FirstName", first_name)
                except:
                    pass

                try:
                    middle_name = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@MiddleName"]
                    winner_person.middle_name = middle_name
                    #print("MiddleName", middle_name)
                except:
                    pass
                try:
                    last_name = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@LastName"]
                    winner_person.last_name = last_name
                    #print("LastName", last_name)
                except:
                    pass
                try:
                    inn_person = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@INN"]
                    winner_person.inn = inn_person
                    #print("INN", inn_person)
                except:
                    pass
                try:
                    address = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@Address"]
                    winner_person.address = address
                    #print("Address", address)
                except:
                    pass
                try:
                    phone = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@Phone"]
                    winner_person.phone = phone
                    #print("Phone", phone)
                except:
                    pass

                try:
                    email = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@Email"]
                    winner_person.email = email
                    #print("Email", email)
                except:
                    pass
                #print("Winner")
                # ==============================Debtors
                # Company
                try:
                    full_name = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                            "ns1:DebtorCompany"][
                            "@FullName"]
                    debtor_company.full_name = full_name

                    #print("DebtorCompanyFullName", full_name)
                except:
                    pass
                try:
                    short_name = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"]["ns1:DebtorPerson"][
                            "@ShortName"]
                    debtor_company.short_name = short_name
                    #print("DebtorCompanyShortName", short_name)
                except:
                    pass

                try:
                    inn = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                            "ns1:DebtorCompany"][
                            "@INN"]
                    debtor_company.inn = inn
                    #print("DebtorPersonINN", inn)
                except:
                    pass
                try:
                    ogrn = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                            "ns1:DebtorCompany"][
                            "@OGRN"]
                    debtor_company.ogrn = ogrn
                    #print("DebtorOGRN", ogrn)
                except:
                    pass

                # DebtorPeson
                try:
                    trade_id = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["@TradeId"]
                    bidding_invitation.trade_id = trade_id
                    #print("BiddingInvitationTradeID", trade_id)
                except:
                    pass
                try:
                    event_time = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["@EventTime"]
                    bidding_invitation.event_time = event_time
                    #print("DebtorPersonEventTime", event_time)
                except:
                    pass
                try:
                    id_efrsb = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:IDEFRSB"]
                    #print("DebtorPersonIDEFRSB", id_efrsb)
                    bidding_invitation.idefrsb = id_efrsb
                except:
                    pass
                try:
                    first_name = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"]["ns1:DebtorPerson"][
                            "@FirstName"]
                    debtor_person.first_name = first_name
                    #print("DebtorPersonFirsName", first_name)
                    # sleep()
                except:
                    pass
                try:
                    last_name = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"]["ns1:DebtorPerson"][
                            "@LastName"]
                    debtor_person.last_name = last_name
                    #print("DebtorPersonLastName", last_name)
                except:
                    pass
                try:
                    middle_name = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"]["ns1:DebtorPerson"][
                            "@MiddleName"]
                    debtor_person.middle_name = middle_name
                    #print("DebtorPersonMiddleName", middle_name)
                except:
                    pass
                try:
                    inn = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"]["ns1:DebtorPerson"][
                            "@INN"]
                    debtor_person.inn = inn
                    #print("DebtorPersonINN", inn)
                except:
                    pass
                try:
                    snils = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"]["ns1:DebtorPerson"][
                            "@SNILS"]
                    debtor_person.snils = snils
                    #print("DebtorPersonSNILS", snils)

                except:
                    pass
                #print("after debtor")

                try:
                    case_number = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:LegalCase"][
                        "@CaseNumber"]
                    legal_case.case_number = case_number
                    #print("CaseNumber", case_number)
                except:
                    pass
                try:
                    court_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:LegalCase"][
                        "@CourtName"]
                    legal_case.court_name = court_name
                    #print("CourtName", court_name)
                except:
                    pass
                try:
                    base = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:LegalCase"]["@Base"]
                    legal_case.base = base
                    #print("Base", base)
                except:
                    pass
                # ArbitrManager
                try:
                    sro_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:ArbitrManager"][
                        "@SROName"]
                    # arbitr_manager.sro = sro_name
                    #print("SroName", sro_name)
                except:
                    pass
                try:
                    reg_num = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:ArbitrManager"][
                        "@RegNum"]
                    arbitr_manager.reg_num = reg_num
                    #print("RegNum", reg_num)
                except:
                    pass
                try:
                    first_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:ArbitrManager"][
                        "@FirstName"]
                    #print(first_name)
                    # sleep(30)
                    arbitr_manager.first_name = first_name
                    #print("ArbitrManagerFirsName", first_name)
                except:
                    pass
                try:
                    last_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:ArbitrManager"][
                        "@LastName"]
                    arbitr_manager.last_name = last_name
                    #print("ArbitrManagerLastName", last_name)
                except:
                    pass
                try:
                    middle_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:ArbitrManager"][
                        "@MiddleName"]
                    arbitr_manager.middle_name = middle_name
                    #print("ArbitrManagerMiddleName", middle_name)
                except:
                    pass
                try:
                    inn = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:ArbitrManager"]["@INN"]
                    arbitr_manager.inn = inn
                    #print("ArbitrINN", inn)
                except:
                    pass

                # TradeOrganizer
                try:
                    first_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeOrganizer"][
                        "ns1:TradeOrganizerPerson"][
                        "@FirstName"]
                    trade_organizer_person.first_name = first_name
                    #print("TradeOrganizerFirstName", first_name)
                except:
                    pass
                try:
                    last_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeOrganizer"][
                        "ns1:TradeOrganizerPerson"][
                        "@LastName"]
                    trade_organizer_person.last_name = last_name
                    #print("TradeOrganizerLastName", last_name)
                except:
                    pass
                try:
                    middle_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeOrganizer"][
                        "ns1:TradeOrganizerPerson"][
                        "@MiddleName"]
                    trade_organizer_person.middle_name = middle_name
                    #print("TradeOrganizerMiddleName", middle_name)
                except:
                    pass
                try:
                    inn = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeOrganizer"][
                        "ns1:TradeOrganizerPerson"]["@INN"]
                    trade_organizer_person.inn = inn
                    #print("TradeOrganizerINN", inn)
                except:
                    pass
                try:
                    snils = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeOrganizer"][
                        "ns1:TradeOrganizerPerson"][
                        "@SNILS"]
                    trade_organizer_person.snils = snils
                    #print("TradeOrganizerSnils", snils)
                except:
                    pass
                # TradeInfo
                try:
                    auction_type = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"][
                        "@AuctionType"]
                    trade_info.auction_type = auction_type
                    #print("AuctionType", auction_type)
                except:
                    pass
                try:
                    form_price = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"][
                        "@FormPrice"]
                    trade_info.form_price = form_price
                    #print("FormPrice", form_price)
                except:
                    pass
                try:
                    time_begin = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:OpenForm"][
                            "@TimeBegin"]
                    open_form.time_begin = time_begin
                    #print("TimeBegin", time_begin)
                except:
                    pass
                try:
                    time_result = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:CloseForm"][
                            "@TimeResult"]
                    close_form.time_result = time_result
                    #print("TimeBegin", time_result)
                except:
                    pass
                try:
                    time_begin = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["OpenForm"][
                            "@TimeBegin"]
                    open_form.time_begin = time_begin
                    #print("TimeBegin", time_begin)
                except:
                    pass
                try:
                    time_result = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["CloseForm"][
                            "@TimeResult"]
                    close_form.time_result = time_result
                    #print("TimeBegin", time_result)
                except:
                    pass

                try:
                    time_end = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:OpenForm"][
                            "@TimeEnd"]
                    open_form.time_end = time_end
                    #print("TimeBegin", time_end)
                except:
                    pass
                try:
                    time_begin_appl = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"][
                            "ns1:Application"][
                            "@TimeBegin"]
                    application.time_begin = time_begin_appl

                    #print("ApplicationTimeBegin", time_begin_appl)
                except:
                    pass
                try:
                    time_end_appl = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"][
                            "ns1:Application"][
                            "@TimeEnd"]
                    application.time_end = time_end_appl

                    #print("ApplicationTimeEnd", time_end_appl)
                except:
                    pass
                try:
                    rules = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"][
                            "ns1:Application"][
                            "ns1:Rules"]
                    application.rules = rules

                    #print("ApplicationTimeEnd", rules)  # "ns1:LotList"
                except:
                    pass
                # lotlist
                try:
                    lot_number = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"]["@LotNumber"]
                    lot.lot_number = lot_number
                    #print("LotNumber", lot_number)
                except:
                    pass
                try:
                    start_price = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"]["ns1:StartPrice"]
                    lot.start_price = start_price

                    #print("ns1:StartPrice", start_price)
                except:
                    pass
                try:
                    step_price = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"][
                            "ns1:StartPrice"]
                    lot.step_price = step_price

                    #print("ns1:StepPrice", step_price)
                except:
                    pass
                try:
                    trade_obj_html = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"][
                            "ns1:TradeObjectHtml"]
                    lot.trade_object_html = trade_obj_html

                    #print("ns1:TradeObjectHtml", trade_obj_html)
                except:
                    pass
                try:
                    price_reduction = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"][
                            "ns1:PriceReduction"]
                    lot.price_reduction = price_reduction

                    #print("ns1:PriceReduction", price_reduction)
                except:
                    pass
                try:
                    participants = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"][
                            "ns1:Participants"]
                    lot.participants = participants

                    #print("ns1:Participants", participants)
                except:
                    pass
                try:
                    payment_info = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"][
                            "ns1:PaymentInfo"]
                    lot.payment_info = payment_info

                    #print("ns1:PaymentInfo", payment_info)
                except:
                    pass
                try:
                    sale_agreement = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:LotList"]["ns1:Lot"][
                            "ns1:SaleAgreement"]
                    lot.sale_agreement = sale_agreement

                    #print("ns1:SaleAgreement", sale_agreement)
                except:
                    pass
                try:
                    id_class = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"][
                            "ns1:Classification"]["ns1:IDClass"]
                    classificaition.idclass = id_class
                    #print("ns1:IDClass", id_class)
                except:
                    pass

                    # Debtor correct path
                    # ==============================Debtors
                    # Company#here was tab
                try:
                    full_name = envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"][
                        "DebtorCompany"]["@FullName"]
                    debtor_company.full_name = full_name
                    #print("DebtorCompanyFullName", full_name)
                except:
                    pass
                try:
                    short_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"]["DebtorCompany"][
                            "@ShortName"]
                    debtor_company.short_name = short_name
                    #print("DebtorCompanyShortName", short_name)
                except:
                    pass

                try:
                    inn = envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"][
                        "DebtorCompany"]["@INN"]
                    debtor_company.inn = inn
                    #print("DebtorCompanyINN", inn)
                except:
                    pass
                try:
                    ogrn = envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"][
                        "DebtorCompany"]["@OGRN"]
                    debtor_company.ogrn = ogrn
                    #print("DebtorOGRN", ogrn)
                except:
                    pass

                # DebtorPeson
                try:
                    trade_id = envelope["SetBiddingInvitation"]["BiddingInvitation"]["@TradeId"]
                    bidding_invitation.trade_id = trade_id
                    #print("BiddingInvitationTradeID", trade_id)
                except:
                    pass
                try:
                    event_time = envelope["SetBiddingInvitation"]["BiddingInvitation"]["@EventTime"]
                    bidding_invitation.event_time = event_time
                    #print("BiddingInvitationEventTime", event_time)
                except:
                    pass
                try:
                    id_efrsb = envelope["SetBiddingInvitation"]["BiddingInvitation"]["IDEFRSB"]
                    bidding_invitation.idefrsb = id_efrsb
                    #print("BiddingInvitationIDEFRSB", id_efrsb)
                    #print(bidding_invitation)
                except:
                    pass
                try:
                    if bidding_invitation.trade_id is not None:
                        bidding_invitation.save()
                        set_bidding_invitation.bidding_invitations = bidding_invitation
                        set_bidding_invitation.save()
                        # body.set_bidding_invitation = set_bidding_invitation
                except Exception as ex:
                    print(ex)

                    # sleep(5)
                try:
                    first_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"]["DebtorPerson"][
                            "@FirstName"]
                    debtor_person.first_name = first_name
                    #print("DebtorPersonFirsName", first_name)
                except:
                    pass
                try:
                    last_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"]["DebtorPerson"][
                            "@LastName"]
                    debtor_person.last_name = last_name
                    #print("DebtorPersonLastName", last_name)
                except:
                    pass
                try:
                    middle_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"]["DebtorPerson"][
                            "@MiddleName"]
                    debtor_person.middle_name = middle_name
                    #print("DebtorPersonMiddleName", middle_name)
                except:
                    pass
                try:
                    inn = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"]["DebtorPerson"][
                            "@INN"]
                    debtor_person.inn = inn
                    #print("DebtorPersonINN", inn)
                except:
                    pass
                try:
                    snils = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"]["DebtorPerson"][
                            "@SNILS"]
                    debtor_person.snils = snils
                    #print("DebtorPersonSNILS", snils)
                except:
                    pass
                try:
                    case_number = envelope["SetBiddingInvitation"]["BiddingInvitation"]["LegalCase"][
                        "@CaseNumber"]
                    legal_case.case_number = case_number
                    #print("CaseNumber", case_number)
                except:
                    pass
                try:
                    court_name = envelope["SetBiddingInvitation"]["BiddingInvitation"]["LegalCase"][
                        "@CourtName"]
                    legal_case.court_name = court_name
                    #print("CourtName", court_name)
                except:
                    pass
                try:
                    base = envelope["SetBiddingInvitation"]["BiddingInvitation"]["LegalCase"]["@Base"]
                    legal_case.base = base
                    #print("Base", base)
                except:
                    pass
                # ArbitrManager
                try:
                    sro_name = envelope["SetBiddingInvitation"]["BiddingInvitation"]["ArbitrManager"][
                        "@SROName"]
                    # !
                    #print("SroName", sro_name)
                except:
                    pass
                try:
                    first_name = envelope["SetBiddingInvitation"]["BiddingInvitation"]["ArbitrManager"][
                        "@FirstName"]
                    arbitr_manager.first_name = first_name
                    #print("ArbitrManagerFirsName", first_name)
                except:
                    pass
                try:
                    last_name = envelope["SetBiddingInvitation"]["BiddingInvitation"]["ArbitrManager"][
                        "@LastName"]
                    arbitr_manager.last_name = last_name
                    #print("ArbitrManagerLastName", last_name)
                except:
                    pass
                try:
                    middle_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["ArbitrManager"][
                            "@MiddleName"]
                    arbitr_manager.middle_name = middle_name
                    #print("ArbitrManagerMiddleName", middle_name)
                except:
                    pass
                try:
                    reg_num = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["ArbitrManager"][
                            "@RegNum"]
                    arbitr_manager.reg_num = reg_num
                    #print("RegNum", reg_num)
                except:
                    pass
                # arbitr_manager.reg_num = reg_num
                try:
                    inn = envelope["SetBiddingInvitation"]["BiddingInvitation"]["ArbitrManager"]["@INN"]
                    arbitr_manager.inn = inn
                    #print("ArbitrINN", inn)
                except:
                    pass

                # TradeOrganizer
                try:
                    first_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerPerson"][
                            "@FirstName"]
                    trade_organizer_person.first_name = first_name
                    #print("TradeOrganizerFirstName", first_name)
                except:
                    pass
                try:
                    last_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerPerson"][
                            "@LastName"]
                    trade_organizer_person.last_name = last_name
                    #print("TradeOrganizerLastName", last_name)
                except:
                    pass
                try:
                    middle_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerPerson"][
                            "@MiddleName"]
                    trade_organizer_person.middle_name = middle_name
                    #print("TradeOrganizerMiddleName", middle_name)
                except:
                    pass
                try:
                    inn = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerPerson"][
                            "@INN"]
                    trade_organizer_person.inn = inn
                    #print("TradeOrganizerINN", inn)
                except:
                    pass
                try:
                    snils = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerPerson"][
                            "@SNILS"]
                    trade_organizer_person.snils = snils
                    #print("TradeOrganizerSnils", snils)
                except:
                    pass

                # TradeOrganizerCompany
                try:
                    full_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerCompany"][
                            "@FullName"]
                    trade_organizer_company.full_name = full_name
                    #print("TradeOrganizerFirstName", full_name)
                except:
                    pass
                try:
                    short_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerCompany"][
                            "@ShortName"]
                    trade_organizer_company.short_name = short_name
                    #print("TradeOrganizerShortName", short_name)
                except:
                    pass
                try:
                    inn = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerCompany"][
                            "@INN"]
                    trade_organizer_company.inn = inn
                    #print("TradeOrganizerCompanyINN", inn)
                except:
                    pass
                try:
                    ogrn = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerCompany"][
                            "@OGRN"]
                    trade_organizer_company.ogrn = ogrn
                    #print("TradeOrganizerOGRN", ogrn)
                except:
                    pass
                if trade_organizer_person.first_name is not None:
                    trade_organizer_person.save()
                    trade_organizer.trade_organizer_person = trade_organizer_person
                    trade_organizer.save()

                if trade_organizer_company.full_name is not None:
                    trade_organizer_company.save()
                    trade_organizer.trade_organizer_company = trade_organizer_company
                    trade_organizer.save()
                # _________
                # TradeInfo
                try:
                    auction_type = envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                        "@AuctionType"]
                    trade_info.auction_type = auction_type
                    #print("AuctionType", auction_type)
                except:
                    pass
                try:
                    form_price = envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                        "@FormPrice"]
                    trade_info.form_price = form_price
                    #print("FormPrice", form_price)
                except:
                    pass
                try:
                    time_begin = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["OpenForm"][
                            "@TimeBegin"]
                    open_form.time_begin = time_begin
                    #print("TimeBegin", time_begin)
                except:
                    pass
                try:
                    time_begin_appl = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "Application"]["@TimeBegin"]
                    application.time_begin = time_begin_appl

                    #print("ApplicationTimeBegin", time_begin_appl)
                except:
                    pass
                try:
                    time_end_appl = envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                        "Application"]["@TimeEnd"]
                    application.time_end = time_end_appl

                    #print("ApplicationTimeEnd", time_end_appl)
                except:
                    pass
                try:
                    rules = envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                        "Application"]["Rules"]
                    application.rules = rules

                    #print("ApplicationTimeEnd", rules)  # "ns1:LotList"
                except:
                    pass
                # lotlist
                try:
                    lot_number = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                            "Lot"]["@LotNumber"]
                    lot.lot_number = lot_number

                    #print("LotNumber", lot_number)
                except:
                    pass
                try:
                    start_price = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                            "Lot"]["StartPrice"]
                    lot.start_price = start_price

                    #print("StartPrice", start_price)
                except:
                    pass
                try:
                    step_price = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "LotList"]["Lot"][
                            "StepPrice"]
                    lot.step_price = step_price

                    #print("StepPrice", step_price)
                except:
                    pass
                try:
                    trade_obj_html = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "LotList"]["Lot"][
                            "TradeObjectHtml"]
                    lot.trade_object_html = trade_obj_html

                    #print("TradeObjectHtml", trade_obj_html)
                except:
                    pass
                try:
                    price_reduction = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "LotList"]["Lot"][
                            "PriceReduction"]
                    lot.price_reduction = price_reduction

                    #print("PriceReduction", price_reduction)
                except:
                    pass
                try:
                    participants = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "LotList"]["Lot"][
                            "Participants"]
                    lot.participants = participants

                    #print("Participants", participants)
                except:
                    pass
                try:
                    payment_info = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "LotList"]["Lot"][
                            "PaymentInfo"]
                    lot.payment_info = payment_info

                    #print("PaymentInfo", payment_info)
                except:
                    pass
                try:
                    sale_agreement = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["LotList"]["Lot"][
                            "SaleAgreement"]
                    lot.sale_agreement = sale_agreement

                    #print("SaleAgreement", sale_agreement)
                except:
                    pass
                try:
                    id_class = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "LotList"]["Lot"][
                            "Classification"]["IDClass"]
                    classificaition.idclass = id_class

                    #print("IDClass", id_class)
                except:
                    pass
               ###########################################################################
                if attach.file_name is not None:
                    attach.save()
                try:

                    if lot.lot_number:
                        lot.save()
                        lot_info.save()
                        lot_list.lot = lot
                        lot_list.save()
                        #print(lot_list)

                except Exception as ex:
                    print(ex, "lotlist")
                    # sleep(5)
                #lot_list.save()
                try:
                    if debtor_person.first_name is not None:
                        debtor_person.save()
                        debtor.debtor_person = debtor_person
                        debtor.save()
                except:
                    pass
                try:
                    if arbitr_manager.first_name is not None:
                        arbitr_manager.save()
                except:
                    pass
                try:
                    if debtor_company.full_name is not None:
                        debtor_company.save()
                        debtor.debtor_company = debtor_company
                        debtor.save()
                except:
                    pass
                try:
                    if failure_trade_result.substantiation is not None:
                        failure_trade_result.save()
                except:
                    pass
                try:
                    if legal_case.case_number is not None:
                        legal_case.save()
                except:
                    pass
                try:
                    if application.time_begin is not None:
                        application.save()
                except:
                    pass
                try:
                    if application_dataa.result is not None:
                        application_dataa.save()
                        application_list.applications_data = application_dataa
                except:
                    pass
                try:
                    if application_list.applications_data is not None:
                        application_list.save()
                except:
                    pass
                try:
                    if winner_company.full_name is not None:
                        winner_company.save()
                except:
                    pass
                # try:
                #     if attach.file_name is not None:
                #         attach.save()
                # except Exception as ex:
                #     #print(ex)
                #     #print("attach")
                #     # sleep(5)

                try:
                    #print(lot_list)
                    if application_session_start.trade_id is not None:
                        application_session_start.lot_list = lot_list
                        application_session_start.save()
                        set_application_session_start.application_session_start = application_session_start
                        set_application_session_start.save()
                except Exception as ex:
                    print(ex)
                    #print("start")
                    # sleep(5)

                try:
                    if application_session_statistic.trade_id is not None:
                        # application_session_statistic.lot_list = lot_list
                        application_session_statistic.attach = attach
                        application_session_statistic.save()
                        set_application_session_statistic.application_session_statistic = application_session_statistic
                        set_application_session_statistic.save()
                except Exception as ex:
                    print(ex)
                    #print("statistic")
                    # sleep(5)

                try:
                    if close_form.time_result is not None:
                        close_form.save()
                        trade_info.close_form = close_form
                except:
                    pass
                try:
                    if open_form.time_begin is not None:
                        open_form.save()
                        trade_info.open_form = open_form
                except:
                    pass
                try:
                    if trade_info.auction_type != None:
                        # trade_info.lot_list = lot_list
                        trade_info.application = application
                        # trade_info.attach = attach
                        trade_info.save()
                except:
                    pass
                try:
                    if winner_person.first_name != None:
                        winner_person.save()
                except:
                    pass
                try:
                    if success_trade_result.price is not None:
                        # success_trade_result.winner_company = winner_company
                        # success_trade_result.winner_person = winner_person
                        success_trade_result.save()
                except:
                    pass
                try:
                    if trade_organizer_person.first_name is not None:
                        trade_organizer_person.save()
                        trade_organizer.trade_organizer_person = trade_organizer_person
                        trade_organizer.save()
                except:
                    pass
                try:
                    if trade_organizer_company.full_name is not None:
                        trade_organizer_company.save()
                        trade_organizer.trade_organizer_company = trade_organizer_company
                        trade_organizer.save()
                except:
                    pass

                # trade_organizer.trade_organizer_person = trade_organizer_person
                # if trade_organizer.trade_organizer_person is not None or trade_organizer.trade_organizer_company is not None:
                # trade_organizer.save()
                # contract_number_model.save()
                # contract_info.contract_number = contract_number_model
                try:
                    if contract_info.contract_number is not None:
                        contract_info.save()
                except:
                    pass
                try:
                    if contract_participant.name is not None:
                        contract_participant.save()
                        contract_participant_list.contract_participant = contract_participant
                        contract_participant_list.save()
                        lot_contract_sale.contract_participant_list = contract_participant_list
                        lot_contract_sale.contract_info = contract_info
                except:
                    pass
                try:
                    if lot_contract_sale.lot_number is not None:
                        lot_contract_sale.save()
                        lot_contract_sale_list.lot_contract_sale = lot_contract_sale
                        lot_contract_sale_list.save()
                        contract_sale.lot_contract_sale_list = lot_contract_sale_list

                except:
                    pass
                try:
                    if contract_sale.trade_id is not None:
                        contract_sale.save()
                        set_contract_sale.contract_sale = contract_sale
                        set_contract_sale.save()
                        body.set_contract_sale = set_contract_sale
                except:
                    pass

                # if bidding_invitation.trade_id is not None:
                try:
                    if bidding_fail.trade_id is not None:
                        # bidding_fail.lot_list = lot_list
                        bidding_fail.save()
                        set_bidding_fail.bidding_fail = bidding_fail
                        set_bidding_fail.save()
                except:
                    pass
                try:
                    if bidding_end.trade_id is not None:
                        # bidding_end.lot_list = lot_list
                        bidding_end.save()
                        set_bidding_end.bidding_end = bidding_end
                        set_bidding_end.save()
                except:
                    pass
                try:
                    if bidding_cancel.trade_id is not None:
                        # bidding_cancel.lot_list = lot_list
                        bidding_cancel.save()
                        set_bidding_cancel.bidding_cancel = bidding_cancel
                        set_bidding_cancel.save()
                except:
                    pass
                try:
                    trade_id = envelope["SetApplicationSessionEnd"]["ApplicationSessionEnd"]["@TradeId"]
                    application_session_end.trade_id = trade_id
                    #print('tradeid', trade_id)

                except:
                    pass
                try:
                    if application_session_end.trade_id is not None:
                        print("="*50)
                        print(lot_list)
                        print("=" * 50)
                        if lot_list:
                            application_session_end.lot_list = lot_list
                            application_session_end.save()
                            set_application_session_end.application_session_end = application_session_end
                            set_application_session_end.save()
                        else:
                            application_session_end.save()
                            set_application_session_end.application_session_end = application_session_end
                            set_application_session_end.save()
                except:
                    pass
                try:
                    if bidding_proccess_info.trade_id is not None:
                        bidding_proccess_info.save()
                except:
                    pass
                try:
                    if bidding_result.trade_id is not None:
                        bidding_result.save()
                        set_bidding_result.bidding_result = bidding_result
                        set_bidding_result.save()
                except:
                    pass

                body.set_bidding_invitation = set_bidding_invitation
                body.set_contract_sale = set_contract_sale
                set_bidding_fail.save()
                body.set_bidding_fail = set_bidding_fail
                body.set_bidding_end = set_bidding_end
                body.set_bidding_cancel = set_bidding_cancel
                # body.set_application_session_start = set_application_session_start
                body.set_application_session_end = set_application_session_end
                # body.set_application_session_statistic = set_application_session_statistic
                body.save()
                envelope_model.body = body
                # envelope_model.body = body_model
                envelope_model.save()
                message_model.id = Id
                message_model.envelope = envelope_model
                message_model.save()
                trade_model.message = message_model
                trade_model.save()
                trade_list.trade = trade_model
                trade_list.save()
                inn = trade_places_inn[j]
                j += 1
                trade_place.inn = inn
                trade_place.trade_list = trade_list
                trade_list.save()
                trade_place.save()
                trade_place_list.trade_place = trade_place
                trade_place_list.save()
                # #print(trade_model.message_id)

                #print("Id", Id)

                # ===================================msJstfgox2Jsr21345Cjs==============================winnerperson

                try:

                    for i in range(len(
                            envelope["SetBiddingResult"]["BiddingResult"]["LotList"]["LotTradeResult"][
                                "Participants"]["Participant"])):
                        #print("Participant", i)
                        try:
                            first_name = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@FirstName"]
                            participant_person.first_name = first_name

                            #print(first_name)

                        except:
                            pass

                        try:
                            last_name = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@LastName"]
                            participant_person.last_name = last_name
                            #print(last_name)
                        except:
                            pass
                        try:
                            middle_name = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@MiddleName"]
                            participant_person.middle_name = middle_name
                            #print(middle_name)
                        except:
                            pass
                        try:
                            inn = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@INN"]
                            participant_person.inn = inn
                            #print(inn)
                        except:
                            pass
                        try:
                            address = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@Address"]
                            participant_person.address = address
                            #print(address)
                        except:
                            pass
                        try:
                            phone = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@Phone"]
                            participant_person.phone = phone
                            #print(phone)
                        except:
                            pass
                        try:
                            email = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@Email"]
                            participant_person.email = email
                            #print(email)
                        except:
                            pass
                        participant_person.save()
                except:
                    pass

                #print("True Dict")
        except:
            pass
        try:
            if type([]) == type(trade["Trade"]["Message"]):

                for message in trade["Trade"]["Message"]:
                    #print(message)
                    bidding_fail = BiddingFail()  # BiddingFail
                    bidding_proccess_info = BiddingProcessInfo()
                    application_session_start = ApplicationSessionStart()
                    application_session_end = ApplicationSessionEnd()
                    bidding_result = BiddingResult()
                    price_info = PriceInfo()
                    application_session_statistic = ApplicationSessionStatistic()
                    lot_statistic = LotStatistic()
                    lot_trade_result = LotTradeResult()
                    success_trade_result = SuccessTradeResult()
                    bidding_state_lot_info = BiddingStateLotInfo()
                    attach = Attach()
                    winner_person = WinnerPerson()
                    winner_company = WinnerCompany()
                    debtor_person = DeptorPerson()
                    debtor_company = DebtorCompany()
                    bidding_invitation = BiddingInvitation()
                    legal_case = LegalCase()
                    arbitr_manager = ArbitrManager()
                    trade_organizer_person = TradeOrganizerPerson()
                    trade_organizer_company = TradeOrganizerCompany()
                    trade_info = TradeInfo()
                    open_form = OpenForm()
                    close_form = CloseForm()
                    application = Application()
                    lot = Lot()
                    lot_list = LotList()
                    bidding_cancel = BiddingCancel()
                    bidding_end = BiddingEnd()
                    classificaition = Classification()
                    participant_person = ParticipantPerson()
                    lot_info = LotInfo()
                    failure_trade_result = FailureTradeResult()
                    application_dataa = ApplicationData()
                    message_model = Message()
                    application_list = ApplicationList()
                    trade_model = Trade()
                    trade_list = TradeList()
                    trade_place = TradePlace()
                    trade_place_list = TradePlaceList()
                    envelope_model = Envelope()
                    body = Body()
                    set_application_session_statistic = SetApplicationSessionStatistic()
                    set_application_session_end = SetApplicationSessionEnd()
                    set_application_session_start = SetApplicationSessionStart()
                    set_bidding_end = SetBiddingEnd()
                    set_bidding_proccess_info = SetBiddingProcessInfo()
                    set_bidding_start = SetBiddingStart()
                    set_bidding_fail = SetBiddingFail()
                    set_bidding_resume = SetBiddingResume()
                    set_bidding_cancel = SetBiddingCancel()
                    set_bidding_result = SetBiddingResult()
                    buyer_company = BuyerCompany()
                    buyer_person = BuyerPerson()
                    bidding_start = BiddingStart()

                    try:
                        id_efrsb = trade["Trade"]["@ID_EFRSB"]
                        #print(id_efrsb)
                        trade_model.id_efrsb = id_efrsb
                    except:
                        pass
                    try:
                        id_external = trade["Trade"]["@ID_EXTERNAL"]
                        trade_model.id_external = id_external
                        #print(id_external)
                    except:
                        pass
                    id = message["@ID"]
                    try:
                        envelop = message["soap:Envelope"]["soap:Body"]
                        envelope = envelop

                    except:
                        pass
                    try:
                        envelop = message["SOAP-ENV:Envelope"]["SOAP-ENV:Body"]
                        envelope = envelop
                    except:
                        pass
                    try:
                        envelop = message["S:Envelope"]["S:Body"]
                        envelope = envelop
                    except:
                        pass
                    try:
                        envelop = message["soapenv:Envelope"]["soapenv:Body"]
                        envelope = envelop
                    except:
                        pass

                    try:

                        envelop = message["soap:Envelope"]["soap:Body"]
                        envelope = envelop
                        # #print(envelope,"envelope for")
                        # sleep(10)
                    except:
                        pass
                    try:
                        envfor = message["soap:Envelope"]
                        envelopefor = envfor

                    except:
                        pass
                    # envelope = message["soap:Envelope"]["soap:Body"]
                    # i += 1
                    try:
                        xmlns_xsi = envelopefor["@xmlns:xsi"]
                        xmlns_xsd = envelopefor["@xmlns:xsd"]
                        xmlns_soap = envelopefor["@xmlns:soap"]
                        #print("xmlns_xsi", xmlns_xsi)
                        #print("xmlns_xsd", xmlns_xsd)
                        #print("xmlns_soap", xmlns_soap)
                    except:
                        pass
                    # #print("ID", id)

                    try:
                        xmlns = envelope["SetApplicationSessionEnd"]["@xmlns"]
                        #print("xmlns", xmlns)
                    except:
                        pass
                    try:
                        xmlns = envelope["SetBiddingProcessInfo"]["@xmlns"]
                        #print("xmlns", xmlns)

                    except:
                        pass
                    try:
                        xmlns = envelope["SetBiddingResult"]["@xmlns"]
                        #print("xmlns", xmlns)

                    except:
                        pass
                    try:
                        xmlns = envelope["SetApplicationSessionStatistic"]["@xmlns"]
                        #print("xmlns", xmlns)

                    except:
                        pass
                    try:
                        trade_id = envelope["SetApplicationSessionEnd"]["ApplicationSessionEnd"]["@TradeId"]

                        application_session_end.trade_id = trade_id
                        #print('tradeid', trade_id)

                    except:
                        pass
                    try:
                        trade_id = envelope["SetBiddingProcessInfo"]["BiddingProccesInfo"]["@TradeId"]
                        bidding_proccess_info.trade_id = trade_id
                        #print('tradeid', trade_id)
                    except:
                        pass
                    try:
                        trade_id = envelope["SetBiddingCancel"]["BiddingCancel"][
                            "@TradeId"]
                        bidding_cancel.trade_id = trade_id
                        # trades_list.trade_id = trade_model
                        #print("TradeId", trade_id)
                    except:
                        pass
                    try:
                        trade_id = envelope["SetBiddingEnd"]["BiddingEnd"][
                            "@TradeId"]
                        bidding_end.trade_id = trade_id
                        # trades_list.trade_id = trade_model
                        #print("TradeId", trade_id)
                    except:
                        pass
                    try:
                        trade_id = envelope["SetBiddingFail"]["BiddingFail"]["@TradeId"]
                        #print(trade_id)
                        bidding_fail.trade_id = trade_id
                        #print("TradeId", trade_id)
                    except:
                        pass
                    try:
                        trade_id = envelope["SetBiddingResult"]["BiddingResult"]["@TradeId"]
                        bidding_result.trade_id = trade_id
                        #print('tradeid', trade_id)
                    except:
                        pass
                    try:
                        trade_id = envelope["SetBiddingStart"]["BiddingStart"]["@TradeId"]
                        bidding_start.trade_id = trade_id
                        #print('tradeid', trade_id)
                    except:
                        pass
                    try:
                        trade_id = envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                            "@TradeId"]
                        application_session_statistic.trade_id = trade_id
                        #print('tradeid', trade_id)
                    except:
                        pass
                    try:
                        trade_id = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"][
                            "@TradeId"]
                        bidding_proccess_info.trade_id = trade_id
                        #print("TradeId", trade_id)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"][
                            "@EventTime"]
                        bidding_proccess_info.event_time = event_time
                        #print("EventTime", event_time)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingCancel"]["BiddingCancel"][
                            "@EventTime"]
                        bidding_cancel.event_time = event_time
                        # trades_list.trade_id = trade_model
                        #print("EventTime", event_time)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingEnd"]["BiddingEnd"][
                            "@EventTime"]
                        bidding_end.event_time = event_time
                        # trades_list.trade_id = trade_model
                        #print("EventTime", event_time)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingFail"]["BiddingFail"][
                            "@EventTime"]
                        bidding_fail.event_time = event_time
                        # trades_list.trade_id = trade_model
                        #print("EventTime", event_time)
                    except:
                        pass
                    try:
                        lot_number = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"]["PriceInfo"][
                            "@LotNumber"]
                        price_info.lot_number = lot_number
                        #print("LotNumber", lot_number)
                    except:
                        print("Some ERror")
                    try:
                        reason = envelope["SetBiddingCancel"]["BiddingCancel"]["@Reason"]
                        #print("Reason", reason)
                        bidding_cancel.reason = reason

                    except:
                        pass
                    try:
                        reason = envelope["SetBiddingFail"]["BiddingFail"]["@Reason"]
                        #print("Reason", reason)
                        bidding_fail.reason = reason

                    except:
                        pass
                    try:
                        reason = envelope["SetBiddingFail"]["BiddingFail"]["LotList"]["BiddingStateLotInfo"]["@Reason"]
                        #print("Reason", reason)
                        bidding_fail.reason = reason

                    except:
                        pass
                    try:
                        new_price = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"]["PriceInfo"][
                            "@NewPrice"]
                        price_info.new_price = new_price
                        #print("NewPrice", new_price)
                    except:
                        print("Some ERror")
                    try:
                        event_time1 = envelope["SetBiddingProcessInfo"]["BiddingProccesInfo"]["@EventTime"]
                        bidding_proccess_info.event_time = event_time1
                        #print("eventtimeProccesInfo", event_time1)
                    except:
                        pass
                    try:
                        event_time2 = envelope["SetApplicationSessionEnd"]["ApplicationSessionEnd"][
                            "@EventTime"]
                        application_session_end.event_time = event_time2
                        #print("eventtimeEnd", event_time2)
                    except:
                        pass
                    try:
                        event_time = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "@EventTime"]
                        application_session_statistic.event_time = event_time
                        #print("eventtimeStat", event_time)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingResult"]["BiddingResult"]["@EventTime"]
                        bidding_result.event_time = event_time
                        #print('eventtime', event_time)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingStart"]["BiddingStart"]["@EventTime"]
                        bidding_start.event_time = event_time
                        #print('eventtime', event_time)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingEnd"]["BiddingEnd"]["@EventTime"]
                        bidding_end.event_time = event_time
                        #print('eventtime', event_time)
                    except:
                        pass
                    try:
                        lot_number = envelope["SetBiddingEnd"]["BiddingEnd"]["@EventTime"]["LotList"]["LotInfo"][
                            "@LotNumber"]
                        lot_info.lot_number = lot_number
                        #print('eventtime', lot_number)
                    except:
                        pass
                    try:
                        date_begin = envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                            "DateBegin"]
                        application_session_statistic.date_begin = date_begin
                        #print("DateBegin", date_begin)
                    except:
                        pass
                    try:
                        lot_number = \
                            envelope["SetApplicationSessionEnd"]["ApplicationSessionEnd"]["LotList"][
                                "LotInfo"][
                                "@LotNumber"]
                        lot_info.lot_number = lot_number

                        #print("LotNumber", lot_number)
                    except:
                        pass
                    try:
                        lot_number = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "LotList"]["LotStatistic"][
                                "@LotNumber"]
                        lot_statistic.lot_number = lot_number
                        #print("LotNumber", lot_number)
                    except:
                        pass
                    try:
                        lot_number = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"][
                                "@LotNumber"]
                        lot_trade_result.lot_number = lot_number
                        #print("LotNumber", lot_number)
                    except:
                        pass
                    try:
                        substantiation = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"][
                                "FailureTradeResult"]["Substantiation"]
                        failure_trade_result.substantiation = substantiation

                        #print("substantiation", substantiation)
                    except:
                        pass
                    try:
                        price = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"][
                                "FailureTradeResult"]["Price"]
                        failure_trade_result.price = price

                        #print("price", price)
                    except:
                        pass
                    try:
                        participants = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"][
                                "Participants"]
                        lot_trade_result.participants = participants

                        #print("Participants", participants)
                    except:
                        pass
                    try:
                        price = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "@Price"]
                        success_trade_result.price = price
                        #print("Price", price)
                    except:
                        pass
                    # winnerCompany
                    try:
                        full_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@FullName"]
                        winner_company.full_name = full_name
                        #print("FullName", full_name)
                    except:
                        pass

                    try:
                        short_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@ShortName"]
                        winner_company.short_name = short_name
                        #print("ShortName", short_name)
                    except:
                        pass
                    try:
                        inn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@INN"]
                        winner_company.inn = inn
                        #print("INN", inn)
                    except:
                        pass
                    try:
                        ogrn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@OGRN"]
                        winner_company.ogrn = ogrn
                        #print("OGRN", ogrn)
                    except:
                        pass
                    try:
                        legal_address = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@LegalAddress"]
                        winner_company.legal_address = legal_address
                        #print("LegalAddress", legal_address)
                    except:
                        pass
                    try:
                        phone = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@Phone"]
                        winner_company.phone = phone
                        #print("Phone", phone)
                    except:
                        pass
                    try:
                        post_address = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@PostAddress"]
                        winner_company.post_address = post_address
                        #print("PostAddress", post_address)
                    except:
                        pass
                    try:
                        email = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@Email"]
                        winner_company.email = email
                        #print("LegalAddress", email)
                    except:
                        pass
                    if winner_person.first_name is not None:
                        winner_person.save()
                    if winner_company.full_name is not None:
                        winner_company.save()
                    try:
                        substantiation = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"][
                                "SuccessTradeResult"]["Substantiation"]
                        success_trade_result.substantiation = substantiation

                        #print("substantiation", substantiation)
                    except:
                        pass
                    try:
                        price = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"][
                                "SuccessTradeResult"]["Price"]
                        success_trade_result.price = price

                        #print("price", price)
                    except:
                        pass
                    # try:
                    #     if success_trade_result.price is not None:
                    #         success_trade_result.winner_company = winner_company
                    #         success_trade_result.winner_person = winner_person
                    #         success_trade_result.save()
                    # except Exception as ex:
                    #     #print(ex)
                    #     #print("tradres")
                    #     sleep(5)
                    # WinnerCompanyEnd
                    try:
                        full_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerCompany"]["@FullName"]
                        buyer_company.full_name = full_name
                        # buyer_company.save()
                        #print("BuyerCompany FullName", full_name)
                    except:
                        pass
                    try:
                        short_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerCompany"]["@ShortName"]
                        buyer_company.short_name = short_name
                        #print("ShortName", short_name)
                    except:
                        pass
                    try:
                        inn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerCompany"]["@INN"]
                        buyer_company.inn = inn
                        #print("INN", inn)
                    except:
                        pass
                    try:
                        ogrn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerCompany"]["@OGRN"]
                        buyer_company.ogrn = ogrn
                        #print("OGRN", ogrn)
                    except:
                        pass

                    if buyer_company.full_name is not None:
                        buyer_company.save()
                    # #TradeOrganizer
                    # try:
                    #     first_name = \
                    #         envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                    #             "TradeOrganizerPerson"][
                    #             "@FirstName"]
                    #     trade_organizer_person.first_name = first_name
                    #     #print("TradeOrganizerFirstName", first_name)
                    # except:
                    #     pass
                    # try:
                    #     last_name = \
                    #         envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                    #             "TradeOrganizerPerson"][
                    #             "@LastName"]
                    #     trade_organizer_person.last_name = last_name
                    #     #print("TradeOrganizerLastName", last_name)
                    # except:
                    #     pass
                    # try:
                    #     middle_name = \
                    #         envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                    #             "TradeOrganizerPerson"][
                    #             "@MiddleName"]
                    #     trade_organizer_person.middle_name = middle_name
                    #     #print("TradeOrganizerMiddleName", middle_name)
                    # except:
                    #     pass
                    # try:
                    #     inn = \
                    #         envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                    #             "TradeOrganizerPerson"][
                    #             "@INN"]
                    #     trade_organizer_person.inn = inn
                    #     #print("TradeOrganizerINN", inn)
                    # except:
                    #     pass
                    # try:
                    #     snils = \
                    #         envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                    #             "TradeOrganizerPerson"][
                    #             "@SNILS"]
                    #     trade_organizer_person.snils = snils
                    #     #print("TradeOrganizerSnils", snils)
                    # except:
                    #     pass
                    # #_________
                    # Winner Person
                    try:
                        first_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["SuccessTradeResult"][
                                "WinnerPerson"]["@FirstName"]

                        winner_person.first_name = first_name
                        winner_person.save()
                        #print("FirstName--------------", first_name)
                    except KeyError as ex:
                        print(ex)
                        #print("except firstName")
                    try:
                        middle_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerPerson"]["@MiddleName"]
                        winner_person.middle_name = middle_name
                        #print("MiddleName---------", middle_name)
                    except:
                        pass
                    try:
                        last_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerPerson"]["@LastName"]
                        winner_person.last_name = last_name
                        #print("LastName------------", last_name)
                    except:
                        pass
                    try:
                        inn_person = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerPerson"]["@INN"]
                        winner_person.inn = inn_person
                        #print("INN", inn_person)
                    except:
                        pass
                    try:
                        address = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerPerson"]["@Address"]
                        winner_person.address = address
                        #print("Address", address)
                    except:
                        pass
                    try:
                        phone = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerPerson"]["@Phone"]
                        winner_person.phone = phone
                        #print("Phone", phone)
                    except:
                        pass

                    try:
                        email = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerPerson"]["@Email"]
                        winner_person.email = email
                        #print("Email", email)
                    except:
                        pass
                    #print("Winner")

                    # =================================================================winnerperson

                    try:
                        for i in range(len(
                                envelope["SetBiddingResult"]["BiddingResult"]["LotList"]["LotTradeResult"][
                                    "Participants"]["Participant"])):
                            #print("Participant", i)
                            try:
                                first_name = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@FirstName"]
                                participant_person.first_name = first_name
                                #print(first_name)

                            except:
                                pass

                            try:
                                last_name = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@LastName"]
                                participant_person.last_name = last_name
                                #print(last_name)
                            except:
                                pass
                            try:
                                middle_name = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@MiddleName"]
                                participant_person.middle_name = middle_name
                                #print(middle_name)
                            except:
                                pass
                            try:
                                inn = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@INN"]
                                participant_person.inn = inn
                                #print(inn)
                            except:
                                pass
                            try:
                                address = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@Address"]
                                participant_person.address = address
                                #print(address)
                            except:
                                pass
                            try:
                                phone = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@Phone"]
                                participant_person.phone = phone
                                #print(phone)
                            except:
                                pass
                            try:
                                email = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@Email"]
                                participant_person.email = email
                                #print(email)
                            except:
                                pass
                            # ===============================

                    except:
                        pass
                    try:
                        first_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"]['ParticipantPerson'][
                                "@FirstName"]
                        participant_person.first_name = first_name
                        #print(first_name)

                    except:
                        pass

                    try:
                        last_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"]['ParticipantPerson'][
                                "@LastName"]
                        participant_person.last_name = last_name
                        #print(last_name)
                    except:
                        pass
                    try:
                        middle_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"]['ParticipantPerson'][
                                "@MiddleName"]
                        participant_person.middle_name = middle_name
                        #print(middle_name)
                    except:
                        pass
                    try:
                        inn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"]['ParticipantPerson'][
                                "@INN"]
                        participant_person.inn = inn
                        #print(inn)
                    except:
                        pass
                    try:
                        address = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"]['ParticipantPerson'][
                                "@Address"]
                        participant_person.address = address
                        #print(address)
                    except:
                        pass
                    try:
                        phone = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"]['ParticipantPerson'][
                                "@Phone"]
                        participant_person.phone = phone
                        #print(phone)
                    except:
                        pass
                    try:
                        email = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"]['ParticipantPerson'][
                                "@Email"]
                        participant_person.email = email
                        #print(email)
                    except:
                        pass
                    # _____________________________________________________-
                    try:
                        for lottraderesult in envelope["SetBiddingResult"]["BiddingResult"]["LotList"][
                            "LotTradeResult"]:
                            # #print(j)
                            # for i in///// range(len(
                            #         envelope["soap:Body"]["SetBiddingResult"]["BiddingResult"]["LotList"]["LotTradeResult"][
                            #             "Participants"]["Participant"])):
                            # #print("Participant", i)
                            try:
                                lot_number = lottraderesult["@LotNumber"]
                                lot_trade_result.lot_number = lot_number
                                #print("LotNumber", lot_number)

                            except:
                                pass
                            try:
                                price = lottraderesult["SuccessTradeResult"]["@Price"]
                                success_trade_result.price = price
                                #print("Price", price)

                            except:
                                pass
                            try:
                                price = lottraderesult["SuccessTradeResult"]["@Price"]
                                success_trade_result.price = price
                                #print(success_trade_result)
                                #print("Price", price)

                            except:
                                pass
                            try:

                                first_name = lottraderesult["SuccessTradeResult"]["WinnerPerson"]["@FirstName"]
                                winner_person.first_name = first_name
                                winner_person.save()
                                #print(first_name, "winner")


                            except:
                                pass

                            try:
                                last_name = \
                                    lottraderesult["SuccessTradeResult"]["WinnerPerson"][
                                        "@LastName"]
                                winner_person.last_name = last_name
                                #print(last_name)
                            except:
                                pass
                            try:
                                middle_name = \
                                    lottraderesult["SuccessTradeResult"]["WinnerPerson"][
                                        "@MiddleName"]
                                winner_person.middle_name = middle_name
                                #print(middle_name)
                            except:
                                pass
                            try:
                                inn = \
                                    lottraderesult["SuccessTradeResult"]["WinnerPerson"][
                                        "@INN"]
                                winner_person.inn = inn
                                #print(inn)
                            except:
                                pass
                            try:
                                address = \
                                    lottraderesult["SuccessTradeResult"]["WinnerPerson"][
                                        "@Address"]
                                winner_person.address = address
                                #print(address)
                            except:
                                pass
                            try:
                                phone = \
                                    lottraderesult["SuccessTradeResult"]["WinnerPerson"][
                                        "@Phone"]
                                winner_person.phone = phone
                                #print(phone)
                            except:
                                pass
                            try:
                                email = \
                                    lottraderesult["SuccessTradeResult"]["WinnerPerson"][
                                        "@Email"]
                                winner_person.email = email
                                #print(email)
                            except:
                                pass

                            # #print("participant")
                            try:
                                print(lottraderesult["Participants"])
                            except:
                                pass
                            try:

                                first_name = lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                    "ParticipantPerson"]["@FirstName"]
                                participant_person.first_name = first_name
                                #print(first_name, "Participant ")

                            except:
                                print("404 participant")

                            try:
                                last_name = \
                                    lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@LastName"]
                                participant_person.last_name = last_name
                                #print(last_name)
                            except:
                                pass
                            try:
                                middle_name = \
                                    lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@MiddleName"]
                                participant_person.middle_name = middle_name
                                #print(middle_name)
                            except:
                                pass
                            try:
                                inn = \
                                    lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@INN"]
                                participant_person.inn = inn
                                #print(inn)
                            except:
                                pass
                            try:
                                address = \
                                    lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@Address"]
                                participant_person.address = address
                                #print(address)
                            except:
                                pass
                            try:
                                phone = \
                                    lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@Phone"]
                                participant_person.phone = phone
                                #print(phone)
                            except:
                                pass
                            try:
                                email = \
                                    lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@Email"]
                                participant_person.email = email
                                #print(email)
                            except:
                                pass
                            # ===============================
                            try:

                                first_name = lottraderesult["Participants"]["Participant"][
                                    "ParticipantPerson"]["@FirstName"]
                                participant_person.first_name = first_name
                                #print(first_name, "Participant ")

                            except:
                                print("404 participant")

                            try:
                                last_name = \
                                    lottraderesult["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@LastName"]
                                participant_person.last_name = last_name
                                #print(last_name)
                            except:
                                pass
                            try:
                                middle_name = \
                                    lottraderesult["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@MiddleName"]
                                participant_person.middle_name = middle_name
                                #print(middle_name)
                            except:
                                pass
                            try:
                                inn = \
                                    lottraderesult["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@INN"]
                                participant_person.inn = inn
                                #print(inn)
                            except:
                                pass
                            try:
                                address = \
                                    lottraderesult["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@Address"]
                                participant_person.address = address
                                #print(address)
                            except:
                                pass
                            try:
                                phone = \
                                    lottraderesult["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@Phone"]
                                participant_person.phone = phone
                                #print(phone)
                            except:
                                pass
                            try:
                                email = \
                                    lottraderesult["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@Email"]
                                participant_person.email = email
                                #print(email)
                            except:
                                pass

                    except:
                        pass
                    # =================================================

                    try:
                        accept_count = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "LotList"]["LotStatistic"][
                                "@AcceptCount"]
                        lot_statistic.accept_count = accept_count
                        #print("accept_count", accept_count)
                    except:
                        pass
                    try:
                        entry_count = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "LotList"]["LotStatistic"][
                                "@EntryCount"]
                        lot_statistic.entry_count = entry_count
                        #print("EntryCount", entry_count)
                    except:
                        pass
                    try:
                        result = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "LotList"]["LotStatistic"]["ApplicationList"]["ApplicationData"]["@Result"]
                        application_dataa.result = result

                        #print("result", result)
                    except:
                        pass

                    # try:
                    #     result = envelope["SetApplicationSessionStatistic"][
                    #         "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["ApplicationList"][
                    #         "ApplicationData"]
                    #     for i in range(len(result)):
                    #         if type(result[i]) == type({}):
                    #             result = result[i]["@Result"]
                    #             application_dataa.result = result
                    #             application_dataa.save()
                    #     #print("result", result)
                    #
                    # except:
                    #     pass
                    try:
                        filename = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "Attach"]["FileName"]
                        print("-" * 50)
                        print("filename", filename)
                        print("-" * 50)
                        attach.file_name = filename

                        # sleep(5)

                    except Exception as ex:
                        print("-" * 50)
                        print(ex)
                        print("-" * 50)

                    try:
                        filename = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "Attach"]["FileName"]
                        print("-" * 50)
                        print("filename", filename)
                        print("-" * 50)
                        attach.file_name = filename

                        #print("filename", filename)
                    except Exception as ex:
                        print("-" * 50)
                        print(ex)
                        print("-" * 50)
                    try:
                        Type = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "Attach"]["Type"]
                        attach.type = Type

                        #print("Type", Type)

                    except:
                        pass

                    try:
                        Type = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "Attach"]["Type"]
                        attach.type = Type

                        #print("Type", Type)
                    except:
                        pass
                    try:
                        Blob = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "Attach"]["Blob"]
                        attach.blob = Blob
                        # attach.save()
                        # #print("Blob", Blob)
                    except:
                        pass
                    try:
                        Blob = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "Attach"]["Blob"]
                        attach.blob = Blob
                        # #print("Blob", Blob)
                    except:
                        pass
                    # message_model.save()
                    # body_model.save()
                    # if buyer_company.full_name is not None:
                    if attach.file_name is not None:
                        attach.save()
                    # buyer_company.save()
                    if failure_trade_result.substantiation is not None:
                        failure_trade_result.buyer_company = buyer_company
                        failure_trade_result.save()
                    if application.time_begin is not None:
                        application.save()
                    if application_dataa.result is not None:
                        application_dataa.save()
                        application_list.applications_data = application_dataa
                    if application_list.applications_data is not None:
                        application_list.save()
                    # envelope_model.body = body_model
                    # try:
                    #     if attach.file_name is not None:
                    #         attach.save()
                    # except Exception as ex:
                    #     #print(ex)
                    #     #print("ATTACH")
                    #     # sleep(5)/

                    # success_trade_result.winner_company = winner_company
                    # success_trade_result.winner_person = winner_person
                    # if success_trade_result.price is not None:
                    #     success_trade_result.save()
                    if lot_info.lot_number is not None:
                        lot_info.save()
                    if lot.lot_number:
                        lot.save()
                        lot_list.lot = lot
                        lot_list.save()

                    if bidding_start.trade_id is not None:
                        bidding_start.lot_list = lot_list
                        bidding_start.save()
                        set_bidding_start.bidding_start = bidding_start


                    if trade_info.auction_type is not None:
                        trade_info.attach = attach
                        trade_info.save()
                    if price_info.new_price is not None:
                        price_info.save()
                    try:
                        lot_list.save()
                        if bidding_fail.trade_id:
                            bidding_fail.lot_list = lot_list
                            bidding_fail.save()
                            set_bidding_fail.bidding_fail = bidding_fail
                            set_bidding_fail.save()
                    except Exception as ex:
                        print("//" * 50)
                        print(ex)
                        print("//" * 50)


                    # #print(bidding_fail)
                    # #print("create bidding fail in list")
                    # sleep(5)
                    # success_trade_result.save()
                    try:
                        if success_trade_result.price is not None:
                            success_trade_result.winner_company = winner_company
                            success_trade_result.winner_person = winner_person
                            success_trade_result.save()
                    except Exception as ex:
                        print(ex)
                        #print("SUCCESSTRADE")
                        #sleep(5)
                    if bidding_proccess_info.trade_id is not None:
                        bidding_proccess_info.price_info = price_info
                        bidding_proccess_info.save()
                        set_bidding_proccess_info.bidding_process_info = bidding_proccess_info
                        set_bidding_proccess_info.save()
                    if bidding_result.trade_id is not None:
                        bidding_result.save()
                        set_bidding_result.bidding_result = bidding_result
                        set_bidding_result.save()

                    bidding_end.lot_list = lot_list
                    bidding_end.save()
                    set_bidding_end.bidding_end = bidding_end
                    set_bidding_end.save()
                    if bidding_cancel.trade_id is not None:
                        bidding_cancel.lot_list = lot_list
                        bidding_cancel.save()
                        set_bidding_cancel.bidding_cancel = bidding_cancel
                        set_bidding_cancel.save()
                    if application_session_start.trade_id is not None:
                        application_session_start.lot_list = lot_list
                        application_session_start.save()
                        set_application_session_start.application_session_start = application_session_start
                        set_application_session_start.save()

                    if application_session_end.trade_id is not None:
                        print("*"*50)
                        print(lot_list)
                        print("*" * 50)
                        application_session_end.lot_list = lot_list
                        application_session_end.save()
                        set_application_session_end.application_session_end = application_session_end
                        set_application_session_end.save()
                    try:
                        if application_session_statistic.trade_id is not None:
                            application_session_statistic.lot_list = lot_list
                            application_session_statistic.attach = attach
                            application_session_statistic.save()
                            set_application_session_statistic.application_session_statistic = application_session_statistic
                            set_application_session_statistic.save()
                    except Exception as ex:
                        print(ex)
                        #print( "in LIST")
                        # sleep(5
                        # )

                    try:
                        body.set_bidding_proccess_info = set_bidding_proccess_info
                        body.set_bidding_fail = set_bidding_fail
                        body.set_bidding_end = set_bidding_end
                        body.set_bidding_cancel = set_bidding_cancel
                        body.set_application_session_start = set_application_session_start
                        body.set_application_session_end = set_application_session_end
                        body.set_application_session_statistic = set_application_session_statistic
                        body.save()
                        envelope_model.body = body
                        envelope_model.save()

                        message_model.id = id
                        message_model.envelope = envelope_model
                        message_model.save()
                        trade_model.message = message_model
                        trade_model.save()
                        trade_list.trade = trade_model
                        trade_list.save()
                        inn = trade_places_inn[j]
                        trade_place.inn = inn
                        j+=1
                        trade_place.trade_list = trade_list
                        trade_list.save()
                        trade_place.save()
                        trade_place_list.trade_place = trade_place
                        trade_place_list.save()
                    except Exception as ex:
                        print(ex)
                        #print("BODY")
                        #sleep(5)

                    #print("InFor___________________________")

        except Exception as ex:
            print(ex)
        #print("END OF")
        #sleep(5)
