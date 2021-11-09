import json
from time import sleep

from xmlinport.views import *
from xmlinport.models import *

def update_products_xml(json_datafile):
    global envelope, envelopefor
    # status  =''
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
    try:
        for i in range(len(data_json["TradePlaceList"]["TradePlace"])):
            try:
                for tradelists in data_json["TradePlaceList"]["TradePlace"][i]["TradeList"]:
                    # #print(tradelists)
                    # trades_list.append(data_json["TradePlaceList"]["TradePlace"][i]["TradeList"])
                    trades_list.append(tradelists)
                    inn = data_json["TradePlaceList"]["TradePlace"][i]["@INN"]
                    trade_places_inn.append(inn)
            except:
                pass

    except Exception as ex:
        pass
        #print("first")

    try:
        for k in range(len(data_json["TradePlaceList"]["TradePlace"]["TradeList"])):
            try:
                tradelists = data_json["TradePlaceList"]["TradePlace"]["TradeList"][k]

                trades_list.append(tradelists)
                inn = data_json["TradePlaceList"]["TradePlace"]["@INN"]
                trade_places_inn.append(inn)
            except Exception as ex:
                pass

    except Exception as ex:
        pass
        #print("second")

    j = -1
    for trade in trades_list:
        #print(type(trades_list))
        #print(type(trade))
        # file = open("otus.txt", "w")
        # file.write(str(trade))
        # file.close()
        # exit()

        # #print(trade)
        # sleep(5)
        j += 1

        try:
            #print("do ifa")
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
                set_bidding_proccess_info = SetBiddingProcessInfo()
                step_price_model = StepPrice()
                annulment = AnnullmentMessage()
                set_annulment = SetAnnulment()
                buyer_company = BuyerCompany()
                buyer_person = BuyerPerson()

                try:
                    id_efrsb = trade["Trade"]["@ID_EFRSB"]
                    # #print(id_efrsb)
                    trade_model.id_efrsb = id_efrsb
                except:
                    pass
                Id = trade["Trade"]["Message"]["@ID"]  # Message ID
                # #print(Id)
                # sleep(20)

                try:
                    id_external = trade["Trade"]["@ID_EXTERNAL"]
                    trade_model.id_external = id_external
                    # #print(id_external)
                except:
                    pass
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

                # try:
                #
                #     envelop = trade["Trade"]["Message"]["SOAP-ENV:Envelope"]["SOAP-ENV:Body"]
                #     envelope = envelop
                # except:
                #     pass
                try:
                    envelop = trade["Trade"]["Message"]["s:Envelope"]["s:Body"]
                    envelope = envelop
                except:
                    pass

                # Содержимое Envelope ниже
                try:
                    message_id = trade["Trade"]["Message"]["@ID"]
                    # trade_model.
                    # #print(message_id)
                except:
                    pass
                try:
                    xmlns_xsi = envelope["@xmlns:xsi"]
                    # #print("xmlns_xsi", xmlns_xsi)
                except:
                    pass
                try:
                    xmlns_xsd = envelope["@xmlns:xsd"]
                    # #print("xmlns_xsd", xmlns_xsd)
                except:
                    pass
                try:
                    xmlns_soap = envelope["@xmlns:soap"]
                    # #print("xmlns_soap", xmlns_soap)
                except:
                    pass
                # Содержимое SetApplicationSessionStatistic ниже
                try:
                    xmlns = envelope["SetApplicationSessionStatistic"]["@xmlns"]
                    # #print("xmlns", xmlns)
                except:
                    pass
                try:
                    xmlns = envelope["SetBiddingFail"]["@xmlns"]
                    # #print("xmlns", xmlns)
                except:
                    pass
                # SetBiddingProcessInfo
                try:
                    xmlns = envelope["SetBiddingProcessInfo"]["@xmlns"]
                    # #print("xmlns", xmlns)
                except:
                    pass
                # Содержимое ApplicationSessionStatistic ниже
                try:
                    trade_id = envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                        "@TradeId"]
                    application_session_statistic.trade_id = trade_id
                    #print('TradeID', trade_id)


                except:
                    pass

                try:
                    trade_id = envelope["SetBiddingFail"]["BiddingFail"][
                        "@TradeId"]

                    bidding_fail.trade_id = trade_id
                    # #print("TradeId", trade_id)

                except:
                    pass
                try:
                    trade_id = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"][
                        "@TradeId"]
                    bidding_proccess_info.trade_id = trade_id
                    #print("TradeId", trade_id)
                    #print("_" * 50)
                except:
                    pass
                try:
                    trade_id = envelope["SetApplicationSessionStart"]["ApplicationSessionStart"][
                        "@TradeId"]
                    application_session_start.trade_id = trade_id
                    #print("TradeId", trade_id)
                    #print("_" * 50)
                except:
                    pass
                try:
                    trade_id = envelope["SetApplicationSessionEnd"]["ApplicationSessionEnd"]["@TradeId"]
                    application_session_end.trade_id = trade_id

                    # #print('tradeid', trade_id)

                except:
                    pass
                try:
                    event_time = envelope["SetApplicationSessionEnd"]["ApplicationSessionEnd"][
                        "@EventTime"]
                    application_session_end.event_time = event_time
                    # #print("eventtimeEnd", event_time2)
                except:
                    pass
                try:
                    lot_number = envelope["SetApplicationSessionEnd"]["ApplicationSessionEnd"][
                        "LotList"]["LotInfo"]["@LotNumber"]
                    lot_info.lot_number = lot_number
                    # #print("eventtimeEnd", event_time2)
                except:
                    pass

                try:
                    trade_id = envelope["SetBiddingResult"]["BiddingResult"][
                        "@TradeId"]
                    bidding_result.trade_id = trade_id
                    # #print("TradeId", trade_id)
                except:
                    pass
                try:
                    substantiation = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"][
                            "FailureTradeResult"]["Substantiation"]
                    failure_trade_result.substantiation = substantiation

                    # #print("substantiation", substantiation)
                except:
                    pass
                try:
                    price = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"][
                            "FailureTradeResult"]["Price"]
                    failure_trade_result.price = price

                    # #print("price", price)
                except:
                    pass
                try:
                    trade_id = envelope["SetBiddingCancel"]["BiddingCancel"][
                        "@TradeId"]
                    bidding_cancel.trade_id = trade_id
                    # #print("TradeId", trade_id)
                except:
                    pass
                try:
                    trade_id = envelope["SetContractSale"]["ContractSale"][
                        "@TradeId"]
                    contract_sale.trade_id = trade_id
                except:
                    pass

                try:
                    event_time = envelope["SetContractSale"]["ContractSale"][
                        "@EventTime"]
                    contract_sale.event_time = event_time
                    # #print("EventTime", event_time)
                except:
                    pass
                try:
                    lot_number = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "@LotNumber"]
                    lot_contract_sale.lot_number = lot_number
                    # #print("LotNumber", lot_number)
                except:
                    pass
                # #winnerCompany
                # try:
                #     full_name = \
                #         envelope["SetBiddingResult"]["BiddingResult"][
                #             "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                #             "WinnerCompany"]["@FullName"]
                #     winner_company.full_name= full_name
                #     ##print("FullName", full_name)
                # except:
                #     pass
                #
                # try:
                #     short_name = \
                #         envelope["SetBiddingResult"]["BiddingResult"][
                #             "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                #             "WinnerCompany"]["@ShortName"]
                #     winner_company.short_name = short_name
                #     ##print("ShortName", short_name)
                # except:
                #     pass
                # try:
                #     inn = \
                #         envelope["SetBiddingResult"]["BiddingResult"][
                #             "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                #             "WinnerCompany"]["@INN"]
                #     winner_company.inn= inn
                #     ##print("INN", inn)
                # except:
                #     pass
                # try:
                #     ogrn = \
                #         envelope["SetBiddingResult"]["BiddingResult"][
                #             "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                #             "WinnerCompany"]["@OGRN"]
                #     winner_company.ogrn= ogrn
                #     ##print("OGRN", ogrn)
                # except:
                #     pass
                # try:
                #     legal_address = \
                #         envelope["SetBiddingResult"]["BiddingResult"][
                #             "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                #             "WinnerCompany"]["@LegalAddress"]
                #     winner_company.legal_address = legal_address
                #     ##print("Address", address)
                # except:
                #     pass
                # #WinnerCompanyEnd
                #print("in if")
                try:
                    contract_number = \
                        envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                            "ContractInfo"][
                            "ContractNumber"]
                    contract_info.contract_number = contract_number
                    # #print("ContractNumber", contract_number)
                except:
                    pass
                try:
                    date_contract = \
                        envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                            "ContractInfo"][
                            "DateContract"]
                    if len(date_contract.split("+")) > 1:
                        date_contract = date_contract.split("+")[0]
                    contract_info.date_contract = date_contract
                    # #print("DateContract", date_contract)
                except:
                    pass

                try:
                    price = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "ContractInfo"][
                        "Price"]
                    contract_info.price = price
                    # #print("Price", price)
                except:
                    pass
                try:
                    name = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "ContractParticipantList"][
                        "ContractParticipant"]["@Name"]
                    contract_participant.name = name
                    # #print("Name", name)
                except:
                    pass
                try:
                    inn = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "ContractParticipantList"][
                        "ContractParticipant"]["@INN"]
                    contract_participant.inn = inn
                    # #print("inn", inn)
                except:
                    pass
                try:
                    ogrn = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "ContractParticipantList"][
                        "ContractParticipant"]["@OGRN"]
                    contract_participant.ogrn = ogrn
                    # #print("OGRN", ogrn)
                except:
                    pass
                try:
                    is_winner = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "ContractParticipantList"][
                        "ContractParticipant"]["@IsWinner"]
                    # contract_participant.is_winner = is_winner
                    contract_participant.is_winner = json.loads(is_winner)

                    # #print("IsWinner", is_winner)
                except:
                    pass
                try:
                    is_buyer = envelope["SetContractSale"]["ContractSale"]["LotContractSaleList"]["LotContractSale"][
                        "ContractParticipantList"][
                        "ContractParticipant"]["@IsBuyer"]
                    # contract_participant.is_buyer = is_buyer
                    contract_participant.is_buyer = json.loads(is_buyer)

                    # #print("IsBuyer", is_buyer)
                except:
                    pass
                # ++++++---------------------------------------------------------------
                try:
                    event_time = envelope["SetApplicationSessionStart"]["ApplicationSessionStart"][
                        "@EventTime"]
                    application_session_start.event_time = event_time
                    # #print("EventTime", event_time)
                except:
                    pass
                try:
                    event_time = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"][
                        "@EventTime"]
                    bidding_proccess_info.event_time = event_time
                    # #print("EventTime", event_time)
                except:
                    pass
                try:
                    event_time = envelope["SetBiddingResult"]["BiddingResult"][
                        "@EventTime"]
                    bidding_result.event_time = event_time
                    # #print("EventTime", event_time)
                except:
                    pass
                try:
                    lot_number = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"][
                        "PriceInfo"]["@LotNumber"]
                    price_info.lot_number = lot_number
                    # #print("LotNumber", lot_number)
                except:
                    pass
                try:
                    lot_number = envelope["SetApplicationSessionStart"]["ApplicationSessionStart"][
                        "LotList"]["LotInfo"]["@LotNumber"]
                    lot_info.lot_number = lot_number
                    # #print("LotNumber", lot_number)
                except:
                    pass
                try:
                    new_price = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"][
                        "PriceInfo"]["@NewPrice"]
                    price_info.new_price = new_price
                    # #print("NewPrice", new_price)
                except:
                    pass
                try:
                    event_time = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"][
                        "@EventTime"]
                    application_session_statistic.event_time = event_time
                    # #print('EventTime', event_time)

                except:
                    pass
                try:
                    event_time = envelope["SetBiddingFail"]["BiddingFail"][
                        "@EventTime"]
                    bidding_fail.event_time = event_time
                    # #print('EventTime', event_time)

                except:
                    pass
                try:
                    event_time = envelope["SetBiddingCancel"]["BiddingCancel"][
                        "@EventTime"]
                    bidding_cancel.event_time = event_time
                    # #print('EventTime', event_time)

                except:
                    pass
                try:
                    date_begin = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"][
                        "DateBegin"]
                    if len(date_begin.split("+")) > 1:
                        date_begin = date_begin.split("+")[0]
                    application_session_statistic.date_begin = date_begin
                    # #print("DateBegin", date_begin)

                except:
                    pass
                    # Содержимое LostLit/LotStatistic ниже
                try:
                    lot_number = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["@LotNumber"]
                    lot_statistic.lot_number = lot_number
                    # #print("LotNumber", lot_number)

                except:
                    pass
                try:
                    lot_number = envelope["SetBiddingResult"][
                        "BiddingResult"]["LotList"]["LotTradeResult"]["@LotNumber"]
                    lot_trade_result.lot_number = lot_number
                    # #print("LotNumber", lot_number)

                except:
                    pass

                try:
                    lot_number = envelope["SetBiddingFail"]["BiddingFail"][
                        "LotList"]["BiddingStateLotInfo"]["@LotNumber"]
                    # #print("LotNumber", lot_number)
                    bidding_state_lot_info.lot_number = lot_number

                except:
                    pass
                try:
                    reason = envelope["SetBiddingFail"]["BiddingFail"][
                        "LotList"]["BiddingStateLotInfo"]["@Reason"]
                    # #print("Reason", reason)
                    bidding_state_lot_info.reason = reason

                except:
                    pass
                try:
                    reason = envelope["SetBiddingCancel"]["BiddingCancel"]["@Reason"]
                    # #print("Reason", reason)
                    bidding_cancel.reason = reason

                except:
                    pass
                try:
                    reason = envelope["SetBiddingFail"]["BiddingFail"]["@Reason"]
                    # #print("Reason", reason)
                    bidding_fail.reason = reason

                except:
                    pass
                try:
                    reason = envelope["SetBiddingFail"]["BiddingFail"]["LotList"]["BiddingStateLotInfo"]["@Reason"]
                    # #print("Reason", reason)
                    bidding_fail.reason = reason

                except:
                    pass
                try:
                    reason = envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                        "LotList"]["BiddingStateLotInfo"]["@Reason"]
                    bidding_state_lot_info.reason = reason
                    # #print("Reason", reason)

                except:
                    pass
                try:
                    accept_count = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["@AcceptCount"]
                    lot_statistic.accept_count = accept_count
                    # #print("AcceptCount", accept_count)

                except:
                    pass
                try:
                    entry_count = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["@EntryCount"]
                    lot_statistic.entry_count = entry_count
                    # #print("EntryCount", entry_count)
                    # "@EntryCount"
                except:
                    pass

                try:
                    result = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["ApplicationList"]["ApplicationData"][
                        "@Result"]
                    application_dataa.result = result
                    # #print("result", result)

                except:
                    pass
                # try:
                #     result = envelope["SetApplicationSessionStatistic"][
                #         "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["ApplicationList"]["ApplicationData"]
                #     for i in range(len(result)):
                #         ##print(i)
                #         sleep(2)
                #         res = result[i]
                #         ##print(res)
                #         sleep(2)
                #         result = res["@Result"]
                #         ##print(result)
                #         sleep(2)
                #         application_dataa.result = result
                #         application_dataa.save()
                #     ##print("result", result)
                #
                # except:
                #     pass
                try:
                    cause_of_refuse = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["ApplicationList"]["ApplicationData"][
                        "@CauseOfRefuse"]
                    application_dataa.cause_of_refuse = cause_of_refuse
                    # #print("CauseOfRefuse", cause_of_refuse)

                except:
                    pass
                try:
                    cause_of_refuse = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["LotList"]["LotStatistic"]["ApplicationList"]["ApplicationData"][
                        "@CauseOfRefuse"]
                    application_dataa.cause_of_refuse = cause_of_refuse
                    # #print("CauseOfRefuse", cause_of_refuse)

                except:
                    pass

                # Содержимое Attach ниже
                try:
                    filename = envelope["SetApplicationSessionStatistic"][
                        "ApplicationSessionStatistic"]["Attach"]["FileName"]
                    attach.file_name = filename
                    # #print("FileName", filename)

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
                try:
                    filename = envelope["SetBiddingInvitation"][
                        "BiddingInvitation"]["Attach"]["FileName"]
                    attach.file_name = filename
                    #print(filename)
                    # #print("FileName", filename)

                except:
                    pass

                try:
                    Type = envelope["SetBiddingInvitation"][
                        "BiddingInvitation"]["Attach"]["Type"]
                    attach.type = Type
                except:
                    pass
                try:
                    Blob = envelope["SetBiddingInvitation"][
                        "BiddingInvitation"]["Attach"]["Blob"]
                    attach.blob = Blob
                except:
                    pass
                try:
                    filename = envelope["SetBiddingInvitation"][
                        "BiddingInvitation"]["TradeInfo"]["Attach"]["FileName"]
                    attach.file_name = filename
                    #print(filename)
                    # #print("FileName", filename)

                except:
                    pass

                try:
                    Type = envelope["SetBiddingInvitation"][
                        "BiddingInvitation"]["TradeInfo"]["Attach"]["Type"]
                    attach.type = Type
                except:
                    pass
                try:
                    Blob = envelope["SetBiddingInvitation"][
                        "BiddingInvitation"]["TradeInfo"]["Attach"]["Blob"]
                    attach.blob = Blob
                except:
                    pass
                try:
                    filename = envelope["SetBiddingFail"][
                        "BiddingFail"]["Attach"]["FileName"]
                    attach.file_name = filename
                    # #print("FileName", filename)

                except:
                    pass
                try:
                    Type = envelope["SetBiddingFail"][
                        "BiddingFail"]["Attach"]["Type"]
                    attach.type = Type
                except:
                    pass
                try:
                    Blob = envelope["SetBiddingFail"][
                        "BiddingFail"]["Attach"]["Blob"]
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
                    # #print("FirstName", first_name)
                except:
                    pass

                try:
                    middle_name = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@MiddleName"]
                    winner_person.middle_name = middle_name
                    # #print("MiddleName", middle_name)
                except:
                    pass
                try:
                    last_name = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@LastName"]
                    winner_person.last_name = last_name
                    # #print("LastName", last_name)
                except:
                    pass
                try:
                    inn_person = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@INN"]
                    winner_person.inn = inn_person
                    # #print("INN", inn_person)
                except:
                    pass
                try:
                    address = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@Address"]
                    winner_person.address = address
                    # #print("Address", address)
                except:
                    pass
                try:
                    phone = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@Phone"]
                    winner_person.phone = phone
                    # #print("Phone", phone)
                except:
                    pass

                try:
                    email = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@Email"]
                    winner_person.email = email
                    # #print("Email", email)
                except:
                    pass
                try:
                    snils = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                            "WinnerPerson"]["@SNILS"]
                    winner_person.snils = snils
                    # #print("Email", email)
                except:
                    pass
                # #print("Winner")
                ##
                try:
                    first_name = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['FailureTradeResult'][
                            "BuyerPerson"]["@FirstName"]
                    buyer_person.first_name = first_name
                    # buyer_company.save()
                    # #print("BuyerCompany FullName", full_name)
                except:
                    pass
                try:
                    middle_name = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['FailureTradeResult'][
                            "BuyerPerson"]["@MiddleName"]
                    buyer_person.middle_name = middle_name
                    # #print("ShortName", short_name)
                except:
                    pass
                try:
                    last_name = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['FailureTradeResult'][
                            "BuyerPerson"]["@LastName"]
                    buyer_person.last_name = last_name
                    # #print("ShortName", short_name)
                except:
                    pass
                try:
                    inn = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['FailureTradeResult'][
                            "BuyerPerson"]["@INN"]
                    buyer_person.inn = inn
                    # #print("INN", inn)
                except:
                    pass

                try:
                    address = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['FailureTradeResult'][
                            "BuyerPerson"]["@Address"]
                    buyer_person.address = address
                    # #print("OGRN", ogrn)
                except:
                    pass
                ##
                try:
                    full_name = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['FailureTradeResult'][
                            "BuyerCompany"]["@FullName"]
                    buyer_company.full_name = full_name
                    # buyer_company.save()
                    # #print("BuyerCompany FullName", full_name)
                except:
                    pass
                try:
                    short_name = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['FailureTradeResult'][
                            "BuyerCompany"]["@ShortName"]
                    buyer_company.short_name = short_name
                    # #print("ShortName", short_name)
                except:
                    pass
                try:
                    inn = \
                        envelope["SetBiddingResult"]["BiddingResult"][
                            "LotList"]["LotTradeResult"]['FailureTradeResult'][
                            "BuyerCompany"]["@INN"]
                    buyer_company.inn = inn
                    # #print("INN", inn)
                except:
                    pass
                # ==============================Debtors
                # Company
                try:
                    full_name = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                            "ns1:DebtorCompany"][
                            "@FullName"]
                    debtor_company.full_name = full_name

                    # #print("DebtorCompanyFullName", full_name)
                except:
                    pass
                try:
                    short_name = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"]["ns1:DebtorPerson"][
                            "@ShortName"]
                    debtor_company.short_name = short_name
                    # #print("DebtorCompanyShortName", short_name)
                except:
                    pass

                try:
                    inn = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                            "ns1:DebtorCompany"][
                            "@INN"]
                    debtor_company.inn = inn
                    # #print("DebtorPersonINN", inn)
                except:
                    pass
                try:
                    ogrn = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                            "ns1:DebtorCompany"][
                            "@OGRN"]
                    debtor_company.ogrn = ogrn
                    # #print("DebtorOGRN", ogrn)
                except:
                    pass
                # Annulment
                try:
                    trade_id = envelope["SetAnnulment"]["AnnulmentMessage"]["@TradeId"]
                    annulment.trade_id = trade_id
                    # #print("BiddingInvitationTradeID", trade_id)
                except:
                    pass
                try:
                    event_time = envelope["SetAnnulment"]["AnnulmentMessage"]["@EventTime"]
                    annulment.event_time = event_time
                    # #print("DebtorPersonEventTime", event_time)
                except:
                    pass
                try:
                    id_annulment = envelope["SetAnnulment"]["AnnulmentMessage"]["ID_Annulment"]
                    annulment.id_annulment = id_annulment
                    # #print("DebtorPersonEventTime", event_time)
                except:
                    pass
                try:
                    reason = envelope["SetAnnulment"]["AnnulmentMessage"]["Reason"]
                    annulment.reason = reason
                    # #print("DebtorPersonEventTime", event_time)
                except:
                    pass
                # DebtorPeson
                try:
                    trade_id = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["@TradeId"]
                    bidding_invitation.trade_id = trade_id
                    # #print("BiddingInvitationTradeID", trade_id)
                except:
                    pass
                try:
                    event_time = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["@EventTime"]
                    bidding_invitation.event_time = event_time
                    # #print("DebtorPersonEventTime", event_time)
                except:
                    pass
                try:
                    id_efrsb = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:IDEFRSB"]
                    # #print("DebtorPersonIDEFRSB", id_efrsb)
                    bidding_invitation.idefrsb = id_efrsb
                except:
                    pass
                try:
                    first_name = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"]["ns1:DebtorPerson"][
                            "@FirstName"]
                    debtor_person.first_name = first_name
                    # #print("DebtorPersonFirsName", first_name)
                    # sleep()
                except:
                    pass
                try:
                    last_name = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"]["ns1:DebtorPerson"][
                            "@LastName"]
                    debtor_person.last_name = last_name
                    # #print("DebtorPersonLastName", last_name)
                except:
                    pass
                try:
                    middle_name = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"]["ns1:DebtorPerson"][
                            "@MiddleName"]
                    debtor_person.middle_name = middle_name
                    # #print("DebtorPersonMiddleName", middle_name)
                except:
                    pass
                try:
                    inn = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"]["ns1:DebtorPerson"][
                            "@INN"]
                    debtor_person.inn = inn
                    # #print("DebtorPersonINN", inn)
                except:
                    pass
                try:
                    snils = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"]["ns1:DebtorPerson"][
                            "@SNILS"]
                    debtor_person.snils = snils
                    # #print("DebtorPersonSNILS", snils)

                except:
                    pass
                # #print("after debtor")

                try:
                    case_number = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:LegalCase"][
                        "@CaseNumber"]
                    legal_case.case_number = case_number
                    # #print("CaseNumber", case_number)
                except:
                    pass
                try:
                    court_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:LegalCase"][
                        "@CourtName"]
                    legal_case.court_name = court_name
                    # #print("CourtName", court_name)
                except:
                    pass
                try:
                    base = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:LegalCase"]["@Base"]
                    legal_case.base = base
                    # #print("Base", base)
                except:
                    pass
                # ArbitrManager
                try:
                    sro_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:ArbitrManager"][
                        "@SROName"]
                    arbitr_manager.sro_name = sro_name
                    # #print("SroName", sro_name)
                except:
                    pass
                try:
                    reg_num = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:ArbitrManager"][
                        "@RegNum"]
                    arbitr_manager.reg_num = reg_num
                    # #print("RegNum", reg_num)
                except:
                    pass
                try:
                    first_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:ArbitrManager"][
                        "@FirstName"]
                    # #print(first_name)
                    # sleep(30)
                    arbitr_manager.first_name = first_name
                    # #print("ArbitrManagerFirsName", first_name)
                except:
                    pass
                try:
                    last_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:ArbitrManager"][
                        "@LastName"]
                    arbitr_manager.last_name = last_name
                    # #print("ArbitrManagerLastName", last_name)
                except:
                    pass
                try:
                    middle_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:ArbitrManager"][
                        "@MiddleName"]
                    arbitr_manager.middle_name = middle_name
                    # #print("ArbitrManagerMiddleName", middle_name)
                except:
                    pass
                try:
                    inn = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:ArbitrManager"]["@INN"]
                    arbitr_manager.inn = inn
                    # #print("ArbitrINN", inn)
                except:
                    pass

                # TradeOrganizer
                try:
                    first_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeOrganizer"][
                        "ns1:TradeOrganizerPerson"][
                        "@FirstName"]
                    trade_organizer_person.first_name = first_name
                    # #print("TradeOrganizerFirstName", first_name)
                except:
                    pass
                try:
                    last_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeOrganizer"][
                        "ns1:TradeOrganizerPerson"][
                        "@LastName"]
                    trade_organizer_person.last_name = last_name
                    # #print("TradeOrganizerLastName", last_name)
                except:
                    pass
                try:
                    middle_name = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeOrganizer"][
                        "ns1:TradeOrganizerPerson"][
                        "@MiddleName"]
                    trade_organizer_person.middle_name = middle_name
                    # #print("TradeOrganizerMiddleName", middle_name)
                except:
                    pass
                try:
                    inn = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeOrganizer"][
                        "ns1:TradeOrganizerPerson"]["@INN"]
                    trade_organizer_person.inn = inn
                    # #print("TradeOrganizerINN", inn)
                except:
                    pass
                try:
                    snils = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeOrganizer"][
                        "ns1:TradeOrganizerPerson"][
                        "@SNILS"]
                    trade_organizer_person.snils = snils
                    # #print("TradeOrganizerSnils", snils)
                except:
                    pass
                # TradeInfo
                try:
                    auction_type = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"][
                        "@AuctionType"]
                    trade_info.auction_type = auction_type
                    # #print("AuctionType", auction_type)
                except:
                    pass
                try:
                    form_price = envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"][
                        "@FormPrice"]
                    trade_info.form_price = form_price
                    # #print("FormPrice", form_price)
                except:
                    pass
                try:
                    time_begin = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:OpenForm"][
                            "@TimeBegin"]
                    open_form.time_begin = time_begin
                    # #print("TimeBegin", time_begin)
                except:
                    pass
                try:
                    time_result = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:CloseForm"][
                            "@TimeResult"]
                    close_form.time_result = time_result
                    # #print("TimeBegin", time_result)
                except:
                    pass
                try:
                    time_begin = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["OpenForm"][
                            "@TimeBegin"]
                    open_form.time_begin = time_begin
                    # #print("TimeBegin", time_begin)
                except:
                    pass
                try:
                    time_result = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["CloseForm"][
                            "@TimeResult"]
                    close_form.time_result = time_result
                    # #print("TimeBegin", time_result)
                except:
                    pass

                try:
                    time_end = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:OpenForm"][
                            "@TimeEnd"]
                    open_form.time_end = time_end
                    # #print("TimeBegin", time_end)
                except:
                    pass
                try:
                    time_begin_appl = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"][
                            "ns1:Application"][
                            "@TimeBegin"]
                    application.time_begin = time_begin_appl

                    # #print("ApplicationTimeBegin", time_begin_appl)
                except:
                    pass
                try:
                    time_end_appl = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"][
                            "ns1:Application"][
                            "@TimeEnd"]
                    application.time_end = time_end_appl

                    # #print("ApplicationTimeEnd", time_end_appl)
                except:
                    pass
                try:
                    rules = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"][
                            "ns1:Application"][
                            "ns1:Rules"]
                    application.rules = rules

                    # #print("ApplicationTimeEnd", rules)  # "ns1:LotList"
                except:
                    pass
                # lotlist
                try:
                    lot_number = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"]["@LotNumber"]
                    lot.lot_number = lot_number
                    # #print("LotNumber", lot_number)
                except:
                    pass
                try:
                    start_price = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"]["ns1:StartPrice"]
                    lot.start_price = start_price

                    # #print("ns1:StartPrice", start_price)
                except:
                    pass
                try:
                    step_price = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"][
                            "ns1:StepPrice"]
                    lot.step_price = step_price

                    # #print("ns1:StepPrice", step_price)
                except:
                    pass
                try:
                    nil = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"][
                            "ns1:StepPrice"]["@xsi:nil"]

                    step_price_model.nil = json.loads(nil)
                    #print(step_price_model.nil)
                    #print("<" * 50)

                except:
                    pass
                try:
                    nil = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                            "Lot"][
                            "StepPrice"]["@xsi:nil"]
                    step_price_model.nil = json.loads(nil)
                    #print(step_price_model.nil)
                    #print("<" * 50)

                except:
                    pass
                try:
                    trade_obj_html = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"][
                            "ns1:TradeObjectHtml"]
                    lot.trade_object_html = trade_obj_html

                    # #print("ns1:TradeObjectHtml", trade_obj_html)
                except:
                    pass
                try:
                    price_reduction = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"][
                            "ns1:PriceReduction"]
                    lot.price_reduction = price_reduction

                    # #print("ns1:PriceReduction", price_reduction)
                except:
                    pass
                try:
                    participants = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"][
                            "ns1:Participants"]
                    lot.participants = participants

                    # #print("ns1:Participants", participants)
                except:
                    pass
                try:
                    payment_info = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"][
                            "ns1:PaymentInfo"]
                    lot.payment_info = payment_info

                    # #print("ns1:PaymentInfo", payment_info)
                except:
                    pass
                try:
                    sale_agreement = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:LotList"]["ns1:Lot"][
                            "ns1:SaleAgreement"]
                    lot.sale_agreement = sale_agreement

                    # #print("ns1:SaleAgreement", sale_agreement)
                except:
                    pass
                try:
                    id_class = \
                        envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"]["ns1:LotList"][
                            "ns1:Lot"][
                            "ns1:Classification"]["ns1:IDClass"]
                    classificaition.idclass = id_class
                    # #print("ns1:IDClass", id_class)
                except:
                    pass

                    # Debtor correct path
                    # ==============================Debtors
                    # Company#here was tab
                try:
                    full_name = envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"][
                        "DebtorCompany"]["@FullName"]
                    debtor_company.full_name = full_name
                    # #print("DebtorCompanyFullName", full_name)
                except:
                    pass
                try:
                    short_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"]["DebtorCompany"][
                            "@ShortName"]
                    debtor_company.short_name = short_name
                    # #print("DebtorCompanyShortName", short_name)
                except:
                    pass

                try:
                    inn = envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"][
                        "DebtorCompany"]["@INN"]
                    debtor_company.inn = inn
                    # #print("DebtorCompanyINN", inn)
                except:
                    pass
                try:
                    ogrn = envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"][
                        "DebtorCompany"]["@OGRN"]
                    debtor_company.ogrn = ogrn
                    # #print("DebtorOGRN", ogrn)
                except:
                    pass

                # DebtorPeson
                try:
                    trade_id = envelope["SetBiddingInvitation"]["BiddingInvitation"]["@TradeId"]
                    bidding_invitation.trade_id = trade_id
                    # #print("BiddingInvitationTradeID", trade_id)
                except:
                    pass
                try:
                    event_time = envelope["SetBiddingInvitation"]["BiddingInvitation"]["@EventTime"]
                    bidding_invitation.event_time = event_time
                    # #print("BiddingInvitationEventTime", event_time)
                except:
                    pass

                try:
                    id_efrsb = envelope["SetBiddingInvitation"]["BiddingInvitation"]["IDEFRSB"]
                    bidding_invitation.idefrsb = id_efrsb
                    # #print("BiddingInvitationIDEFRSB", id_efrsb)
                    # #print(bidding_invitation)
                except:
                    pass
                # try:
                #     if bidding_invitation.trade_id is not None:
                #         if trade_organizer.pk is not None:
                #             bidding_invitation.trade_ogranizer = trade_organizer
                #         if arbitr_manager.first_name is not None:
                #             bidding_invitation.arbitr_manager = arbitr_manager
                #         bidding_invitation.save()
                #         set_bidding_invitation.bidding_invitations = bidding_invitation
                #         set_bidding_invitation.save()
                #         body.set_bidding_invitation = set_bidding_invitation
                #
                # except:
                #     pass

                # sleep(5)
                try:
                    first_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"]["DebtorPerson"][
                            "@FirstName"]
                    debtor_person.first_name = first_name
                    # #print("DebtorPersonFirsName", first_name)
                except:
                    pass
                try:
                    last_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"]["DebtorPerson"][
                            "@LastName"]
                    debtor_person.last_name = last_name
                    # #print("DebtorPersonLastName", last_name)
                except:
                    pass
                try:
                    middle_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"]["DebtorPerson"][
                            "@MiddleName"]
                    debtor_person.middle_name = middle_name
                    # #print("DebtorPersonMiddleName", middle_name)
                except:
                    pass
                try:
                    inn = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"]["DebtorPerson"][
                            "@INN"]
                    debtor_person.inn = inn
                    # #print("DebtorPersonINN", inn)
                except:
                    pass
                try:
                    snils = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["Debtor"]["DebtorPerson"][
                            "@SNILS"]
                    debtor_person.snils = snils
                    # #print("DebtorPersonSNILS", snils)
                except:
                    pass
                try:
                    case_number = envelope["SetBiddingInvitation"]["BiddingInvitation"]["LegalCase"][
                        "@CaseNumber"]
                    legal_case.case_number = case_number
                    # #print("CaseNumber", case_number)
                except:
                    pass
                try:
                    court_name = envelope["SetBiddingInvitation"]["BiddingInvitation"]["LegalCase"][
                        "@CourtName"]
                    legal_case.court_name = court_name
                    # #print("CourtName", court_name)
                except:
                    pass
                try:
                    base = envelope["SetBiddingInvitation"]["BiddingInvitation"]["LegalCase"]["@Base"]
                    legal_case.base = base
                    # #print("Base", base)
                except:
                    pass
                # ArbitrManager
                try:
                    sro_name = envelope["SetBiddingInvitation"]["BiddingInvitation"]["ArbitrManager"][
                        "@SROName"]
                    # !
                    # #print("SroName", sro_name)
                except:
                    pass
                try:
                    first_name = envelope["SetBiddingInvitation"]["BiddingInvitation"]["ArbitrManager"][
                        "@FirstName"]
                    arbitr_manager.first_name = first_name
                    # #print("ArbitrManagerFirsName", first_name)
                except:
                    pass
                try:
                    last_name = envelope["SetBiddingInvitation"]["BiddingInvitation"]["ArbitrManager"][
                        "@LastName"]
                    arbitr_manager.last_name = last_name
                    # #print("ArbitrManagerLastName", last_name)
                except:
                    pass
                try:
                    middle_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["ArbitrManager"][
                            "@MiddleName"]
                    arbitr_manager.middle_name = middle_name
                    # #print("ArbitrManagerMiddleName", middle_name)
                except:
                    pass
                try:
                    reg_num = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["ArbitrManager"][
                            "@RegNum"]
                    arbitr_manager.reg_num = reg_num
                    # #print("RegNum", reg_num)
                except:
                    pass
                # arbitr_manager.reg_num = reg_num
                try:
                    inn = envelope["SetBiddingInvitation"]["BiddingInvitation"]["ArbitrManager"]["@INN"]
                    arbitr_manager.inn = inn
                    # #print("ArbitrINN", inn)
                except:
                    pass

                # TradeOrganizer
                try:
                    first_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerPerson"][
                            "@FirstName"]
                    trade_organizer_person.first_name = first_name
                    # #print("TradeOrganizerFirstName", first_name)
                except:
                    pass
                try:
                    last_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerPerson"][
                            "@LastName"]
                    trade_organizer_person.last_name = last_name
                    # #print("TradeOrganizerLastName", last_name)
                except:
                    pass
                try:
                    middle_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerPerson"][
                            "@MiddleName"]
                    trade_organizer_person.middle_name = middle_name
                    # #print("TradeOrganizerMiddleName", middle_name)
                except:
                    pass
                try:
                    inn = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerPerson"][
                            "@INN"]
                    trade_organizer_person.inn = inn
                    # #print("TradeOrganizerINN", inn)
                except:
                    pass
                try:
                    snils = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerPerson"][
                            "@SNILS"]
                    trade_organizer_person.snils = snils
                    # #print("TradeOrganizerSnils", snils)
                except:
                    pass

                # TradeOrganizerCompany
                try:
                    full_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerCompany"][
                            "@FullName"]
                    trade_organizer_company.full_name = full_name
                    # #print("TradeOrganizerFirstName", full_name)
                except:
                    pass
                try:
                    short_name = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerCompany"][
                            "@ShortName"]
                    trade_organizer_company.short_name = short_name
                    # #print("TradeOrganizerShortName", short_name)
                except:
                    pass
                try:
                    inn = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerCompany"][
                            "@INN"]
                    trade_organizer_company.inn = inn
                    # #print("TradeOrganizerCompanyINN", inn)
                except:
                    pass
                try:
                    ogrn = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                            "TradeOrganizerCompany"][
                            "@OGRN"]
                    trade_organizer_company.ogrn = ogrn
                    # #print("TradeOrganizerOGRN", ogrn)
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
                    # #print("AuctionType", auction_type)
                except:
                    pass
                try:
                    date_publish_smi = envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                        "DatePublishSMI"]
                    trade_info.date_publish_smi = date_publish_smi
                    # #print("AuctionType", auction_type)
                except:
                    pass
                try:
                    form_price = envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                        "@FormPrice"]
                    trade_info.form_price = form_price
                    # #print("FormPrice", form_price)
                except:
                    pass
                try:
                    time_begin = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["OpenForm"][
                            "@TimeBegin"]
                    open_form.time_begin = time_begin
                    # #print("TimeBegin", time_begin)
                except:
                    pass
                try:
                    time_begin_appl = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "Application"]["@TimeBegin"]
                    application.time_begin = time_begin_appl

                    # #print("ApplicationTimeBegin", time_begin_appl)
                except:
                    pass
                try:
                    time_end_appl = envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                        "Application"]["@TimeEnd"]
                    application.time_end = time_end_appl

                    # #print("ApplicationTimeEnd", time_end_appl)
                except:
                    pass
                try:
                    rules = envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                        "Application"]["Rules"]
                    application.rules = rules

                    # #print("ApplicationTimeEnd", rules)  # "ns1:LotList"
                except:
                    pass
                # lotlist
                try:
                    lot_number = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                            "Lot"]["@LotNumber"]
                    lot.lot_number = lot_number

                    # #print("LotNumber", lot_number)
                except:
                    pass
                try:
                    lot_number = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["LotList"][
                            "Lot"]["@LotNumber"]
                    lot.lot_number = lot_number

                    # #print("LotNumber", lot_number)
                except:
                    pass
                try:
                    start_price = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                            "Lot"]["StartPrice"]
                    lot.start_price = start_price

                    # #print("StartPrice", start_price)
                except:
                    pass
                try:
                    step_price = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "LotList"]["Lot"][
                            "StepPrice"]
                    lot.step_price = step_price

                    # #print("StepPrice", step_price)
                except:
                    pass
                try:
                    trade_obj_html = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "LotList"]["Lot"][
                            "TradeObjectHtml"]
                    lot.trade_object_html = trade_obj_html

                    # #print("TradeObjectHtml", trade_obj_html)
                except:
                    pass
                try:
                    price_reduction = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "LotList"]["Lot"][
                            "PriceReduction"]
                    lot.price_reduction = price_reduction

                    # #print("PriceReduction", price_reduction)
                except:
                    pass
                try:
                    participants = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "LotList"]["Lot"][
                            "Participants"]
                    lot.participants = participants

                    # #print("Participants", participants)
                except:
                    pass
                try:
                    payment_info = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "LotList"]["Lot"][
                            "PaymentInfo"]
                    lot.payment_info = payment_info

                    # #print("PaymentInfo", payment_info)
                except:
                    pass
                try:
                    sale_agreement = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["LotList"]["Lot"][
                            "SaleAgreement"]
                    lot.sale_agreement = sale_agreement

                    # #print("SaleAgreement", sale_agreement)
                except:
                    pass
                try:
                    id_class = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                            "LotList"]["Lot"][
                            "Classification"]["IDClass"]
                    classificaition.idclass = id_class

                    # #print("IDClass", id_class)
                except:
                    pass
                ###########################################################################
                try:
                    if attach.file_name is not None:
                        attach.save()
                except Exception as ex:
                    #print("Attach EX" * 50)
                    pass
                try:
                    if step_price_model.nil is not None:
                        step_price_model.save()
                        lot.step_price = step_price_model
                except:
                    pass
                try:

                    if lot.lot_number:
                        lot.save()
                        #print(lot)
                        lot_list.lot = lot
                        lot_list.save()
                except Exception as ex:
                    pass
                try:
                    if lot_info.lot_number:
                        lot_info.save()
                        lot_list.lot_info = lot_info
                        lot_list.save()
                except:
                    pass

                try:
                    lot_type = \
                        envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                            "Lot"]
                    #print("SAVE POINT" * 50)
                    if type(lot_type) == type([]):
                        for lot_i in range(len(lot_type)):
                            lot = Lot()
                            lot_list = LotList()
                            trade_info = TradeInfo()

                            try:
                                auction_type = envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                                    "@AuctionType"]
                                trade_info.auction_type = auction_type
                                # #print("AuctionType", auction_type)
                            except:
                                pass
                            try:
                                form_price = envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                                    "@FormPrice"]
                                trade_info.form_price = form_price
                                # #print("FormPrice", form_price)
                            except:
                                pass
                            try:
                                time_begin = \
                                    envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["OpenForm"][
                                        "@TimeBegin"]
                                open_form.time_begin = time_begin
                                # #print("TimeBegin", time_begin)
                            except:
                                pass
                            try:
                                time_begin_appl = \
                                    envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                                        "Application"]["@TimeBegin"]
                                application.time_begin = time_begin_appl

                                # #print("ApplicationTimeBegin", time_begin_appl)
                            except:
                                pass
                            try:
                                time_end_appl = envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                                    "Application"]["@TimeEnd"]
                                application.time_end = time_end_appl

                                # #print("ApplicationTimeEnd", time_end_appl)
                            except:
                                pass
                            try:
                                rules = envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"][
                                    "Application"]["Rules"]
                                application.rules = rules

                                # #print("ApplicationTimeEnd", rules)  # "ns1:LotList"
                            except:
                                pass
                            try:
                                lot_number = \
                                    envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                                        "Lot"][lot_i]["@LotNumber"]
                                lot.lot_number = lot_number
                                #print("LotNumber", lot_number)
                            except:
                                pass
                            try:
                                start_price = \
                                    envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                                        "Lot"][lot_i]["StartPrice"]
                                lot.start_price = start_price

                                #print("StartPrice", start_price)
                            except:
                                pass
                            try:
                                step_price = \
                                    envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                                        "Lot"][lot_i][
                                        "StepPrice"]
                                lot.step_price = step_price

                                #print("StepPrice", step_price)
                            except:
                                pass
                            try:
                                nil = \
                                    envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                                        "Lot"][lot_i][
                                        "StepPrice"]["@xsi:nil"]
                                step_price_model.nil = json.loads(nil)


                            except:
                                pass

                            try:
                                trade_obj_html = \
                                    envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                                        "Lot"][lot_i][
                                        "TradeObjectHtml"]
                                lot.trade_object_html = trade_obj_html

                                #print("TradeObjectHtml", trade_obj_html)
                            except:
                                pass
                            try:
                                price_reduction = \
                                    envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                                        "Lot"][lot_i][
                                        "PriceReduction"]
                                lot.price_reduction = price_reduction
                            except:
                                pass
                            try:
                                participants = \
                                    envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                                        "Lot"][lot_i][
                                        "Participants"]
                                lot.participants = participants

                                #print("Participants", participants)
                            except:
                                pass
                            try:
                                payment_info = \
                                    envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                                        "Lot"][lot_i][
                                        "PaymentInfo"]
                                lot.payment_info = payment_info

                                #print("PaymentInfo", payment_info)
                            except:
                                pass
                            try:
                                sale_agreement = \
                                    envelope["SetBiddingInvitation"]["BiddingInvitation"]["LotList"]["Lot"][lot_i][
                                        "SaleAgreement"]
                                lot.sale_agreement = sale_agreement
                            except:
                                pass
                            try:
                                id_class = \
                                    envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                                        "Lot"][lot_i][
                                        "Classification"]["IDClass"]
                                classificaition.idclass = id_class
                                # #print("ns1:IDClass", id_class)
                            except:
                                pass
                            #print(lot)
                            # exit()
                            lot.save()
                            lot_list.lot = lot
                            lot_list.save()
                            #print(lot)

                except Exception as ex:
                    pass
                    #print("lot list type ex" * 50)

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

                try:
                    # #print(lot_list)
                    if application_session_start.trade_id is not None:
                        if lot_info.lot_number is not None:
                            application_session_start.lot_list = lot_list

                        application_session_start.save()
                        set_application_session_start.application_session_start = application_session_start
                        set_application_session_start.save()
                        body.set_application_session_start = set_application_session_start


                except Exception as ex:
                    pass
                    #print("EX" * 50)

                try:
                    if lot_statistic.lot_number is not None:
                        lot_statistic.save()
                        lot_list.lot_statistic = lot_statistic
                        lot_list.save()
                except:
                    pass
                try:
                    if application_session_statistic.trade_id is not None:
                        if lot_statistic.lot_number is not None:
                            application_session_statistic.lot_list = lot_list
                        application_session_statistic.attach = attach
                        application_session_statistic.save()
                        set_application_session_statistic.application_session_statistic = application_session_statistic
                        set_application_session_statistic.save()
                        body.set_application_session_statistic = set_application_session_statistic

                except Exception as ex:
                    pass
                    #print("statistic")
                    # #print("statistic")
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
                        trade_info.application = application
                        trade_info.lot_list = lot_list
                        if attach.file_name is not None:
                            trade_info.attach = attach
                        trade_info.save()
                except Exception as ex:
                    pass
                    #print("EXCEPTION" * 50)

                try:
                    if buyer_person.first_name is not None:
                        buyer_person.save()
                except:
                    pass
                try:
                    if buyer_company.full_name is not None:
                        buyer_company.save()
                        #print(buyer_company)
                        #print(">" * 50)
                except Exception as ex:
                    pass
                    #print(">" * 50)
                try:
                    if success_trade_result.price is not None:
                        if winner_company.full_name is not None:
                            success_trade_result.winner_company = winner_company
                        if winner_person.first_name is not None:
                            success_trade_result.winner_person = winner_person
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
                        body.set_contract_sale = set_contract_sale


                except:
                    pass
                try:
                    if contract_sale.trade_id is not None:
                        contract_sale.save()
                        set_contract_sale.contract_sale = contract_sale
                        set_contract_sale.save()
                        # body.set_contract_sale = set_contract_sale
                except:
                    pass
                try:
                    if bidding_state_lot_info.lot_number is not None:
                        bidding_state_lot_info.save()
                        lot_list.bidding_state_lot_info = bidding_state_lot_info
                        lot_list.save()
                except:
                    pass
                try:
                    if bidding_state_lot_info.lot_number is not None:
                        bidding_state_lot_info.save()
                except:
                    pass
                # if bidding_invitation.trade_id is not None:
                try:
                    if bidding_fail.trade_id is not None:
                        if attach.file_name is not None:
                            bidding_fail.attach = attach
                        if bidding_state_lot_info.lot_number is not None:
                            bidding_fail.lot_list = lot_list
                        bidding_fail.save()
                        set_bidding_fail.bidding_fail = bidding_fail
                        set_bidding_fail.save()
                        body.set_bidding_fail = set_bidding_fail

                except:
                    pass
                try:
                    if annulment.trade_id is not None:
                        annulment.save()
                        set_annulment.annulment_message = annulment
                        set_annulment.save()
                        body.set_annulment = set_annulment
                except Exception as ex:
                    pass
                    #print(":" * 50)
                try:
                    if bidding_end.trade_id is not None:
                        # lot_list.save()
                        # bidding_end.lot_list = lot_list
                        bidding_end.save()
                        set_bidding_end.bidding_end = bidding_end
                        set_bidding_end.save()
                        body.set_bidding_end = set_bidding_end

                except:
                    pass

                try:
                    if bidding_cancel.trade_id is not None:
                        # lot_list.save()
                        # bidding_cancel.lot_list = lot_list
                        bidding_cancel.save()
                        set_bidding_cancel.bidding_cancel = bidding_cancel
                        set_bidding_cancel.save()
                        body.set_bidding_cancel = set_bidding_cancel

                except:
                    pass

                try:
                    if application_session_end.trade_id is not None:
                        # lot_list.save()
                        if lot_info.lot_number is not None:
                            application_session_end.lot_list = lot_list
                        application_session_end.save()
                        set_application_session_end.application_session_end = application_session_end
                        set_application_session_end.save()
                        body.set_application_session_end = set_application_session_end

                except:
                    pass
                try:
                    if bidding_start.trade_id is not None:
                        bidding_start.save()
                        set_bidding_start.bidding_start = bidding_start
                except:
                    pass
                try:
                    if price_info.new_price is not None:
                        price_info.save()
                except:
                    pass
                try:

                    if bidding_proccess_info.trade_id is not None:
                        bidding_proccess_info.price_info = price_info
                        bidding_proccess_info.save()
                        set_bidding_proccess_info.bidding_process_info = bidding_proccess_info
                        body.set_bidding_proccess_info = set_bidding_proccess_info

                except:
                    pass
                try:
                    if bidding_invitation.trade_id is not None:
                        if trade_organizer.pk is not None:
                            bidding_invitation.trade_ogranizer = trade_organizer
                        if arbitr_manager.first_name is not None:
                            bidding_invitation.arbitr_manager = arbitr_manager
                        if legal_case.case_number is not None:
                            bidding_invitation.legal_case = legal_case
                        if trade_info.auction_type is not None:
                            bidding_invitation.trade_info = trade_info
                        if debtor.pk is not None:
                            bidding_invitation.debtor = debtor

                        bidding_invitation.save()
                        set_bidding_invitation.bidding_invitations = bidding_invitation
                        set_bidding_invitation.save()
                        body.set_bidding_invitation = set_bidding_invitation

                except:
                    pass
                try:
                    if lot_trade_result.lot_number is not None:
                        lot_trade_result.save()
                        lot_list.lot_trade_result = lot_trade_result
                        lot_list.save()
                except:
                    pass
                try:
                    if bidding_result.trade_id is not None:
                        if lot_trade_result.lot_number is not None:
                            bidding_result.lot_list = lot_list
                        if attach.file_name is not None:
                            bidding_result.attach = attach

                        bidding_result.save()
                        set_bidding_result.bidding_result = bidding_result
                        set_bidding_result.save()
                        body.set_bidding_result = set_bidding_result

                except:
                    pass

                # body.set_contract_sale = set_contract_sale
                # set_bidding_fail.save()
                # body.set_bidding_fail = set_bidding_fail
                # body.set_bidding_end = set_bidding_end
                # body.set_bidding_cancel = set_bidding_cancel
                # body.set_application_session_start = set_application_session_start
                # body.set_application_session_statistic = set_application_session_statistic
                # body.set_bidding_invitation = set_bidding_invitation
                # body.set_application_session_end = set_application_session_end
                try:
                    body.save()
                except Exception as ex:
                    pass
                    #print("*" * 50)
                    #print(body)
                    #print("*" * 50)

                # #print("*" * 50)
                # #print(body)
                # #print("*" * 50)
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
                # j += 1
                trade_place.inn = inn
                trade_place.trade_list = trade_list
                trade_list.save()
                trade_place.save()
                trade_place_list.trade_place = trade_place
                trade_place_list.save()
                # ##print(trade_model.message_id)

                # #print("Id", Id)

                # ===================================msJstfgox2Jsr21345Cjs==============================winnerperson

                try:

                    for i in range(len(
                            envelope["SetBiddingResult"]["BiddingResult"]["LotList"]["LotTradeResult"][
                                "Participants"]["Participant"])):
                        # #print("Participant", i)
                        try:
                            first_name = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@FirstName"]
                            participant_person.first_name = first_name

                            # #print(first_name)

                        except:
                            pass

                        try:
                            last_name = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@LastName"]
                            participant_person.last_name = last_name
                            # #print(last_name)
                        except:
                            pass
                        try:
                            middle_name = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@MiddleName"]
                            participant_person.middle_name = middle_name
                            # #print(middle_name)
                        except:
                            pass
                        try:
                            inn = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@INN"]
                            participant_person.inn = inn
                            # #print(inn)
                        except:
                            pass
                        try:
                            address = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@Address"]
                            participant_person.address = address
                            # #print(address)
                        except:
                            pass
                        try:
                            phone = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@Phone"]
                            participant_person.phone = phone
                            # #print(phone)
                        except:
                            pass
                        try:
                            email = \
                                envelope["SetBiddingResult"]["BiddingResult"][
                                    "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                    'ParticipantPerson'][
                                    "@Email"]
                            participant_person.email = email
                            # #print(email)
                        except:
                            pass
                        participant_person.save()
                except:
                    pass

                # #print("True Dict")
        except Exception as ex:
            pass
            #print("From dict")
        try:
            if type([]) == type(trade["Trade"]["Message"]):

                for message in trade["Trade"]["Message"]:
                    # message = trade["Trade"]["Message"][message]
                    #print(len(trade["Trade"]["Message"]))

                    # #print(message)
                    # exit()
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
                    debtor = Debtor()
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
                    participant_company = ParticipantCompany()
                    participant = Participant()
                    participants_model = Participants()
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
                    buyer = Buyer()
                    buyer_person = BuyerPerson()
                    bidding_start = BiddingStart()
                    step_price_model = StepPrice()
                    annulment = AnnullmentMessage()
                    set_annulment = SetAnnulment()
                    try:
                        id_efrsb = trade["Trade"]["@ID_EFRSB"]
                        # #print(id_efrsb)
                        trade_model.id_efrsb = id_efrsb
                    except:
                        pass
                    try:
                        id_external = trade["Trade"]["@ID_EXTERNAL"]
                        trade_model.id_external = id_external
                        # #print(id_external)
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
                        # #print("xmlns_xsi", xmlns_xsi)
                        # #print("xmlns_xsd", xmlns_xsd)
                        # #print("xmlns_soap", xmlns_soap)
                    except:
                        pass
                    # ##print("ID", id)

                    try:
                        xmlns = envelope["SetApplicationSessionEnd"]["@xmlns"]
                        # #print("xmlns", xmlns)
                    except:
                        pass
                    try:
                        xmlns = envelope["SetBiddingProcessInfo"]["@xmlns"]
                        # #print("xmlns", xmlns)

                    except:
                        pass
                    try:
                        xmlns = envelope["SetBiddingResult"]["@xmlns"]
                        # #print("xmlns", xmlns)

                    except:
                        pass
                    try:
                        xmlns = envelope["SetApplicationSessionStatistic"]["@xmlns"]
                        # #print("xmlns", xmlns)

                    except:
                        pass
                    try:
                        trade_id = envelope["SetApplicationSessionEnd"]["ApplicationSessionEnd"]["@TradeId"]

                        application_session_end.trade_id = trade_id
                        # #print('tradeid', trade_id)

                    except:
                        pass
                    try:
                        trade_id = envelope["SetBiddingProcessInfo"]["BiddingProccesInfo"]["@TradeId"]
                        bidding_proccess_info.trade_id = trade_id
                        # #print('tradeid', trade_id)
                    except:
                        pass
                    try:
                        trade_id = envelope["SetBiddingCancel"]["BiddingCancel"][
                            "@TradeId"]
                        bidding_cancel.trade_id = trade_id
                        # #print("TradeId", trade_id)
                    except:
                        pass
                    try:
                        trade_id = envelope["SetBiddingEnd"]["BiddingEnd"][
                            "@TradeId"]
                        bidding_end.trade_id = trade_id
                        #print("BiddingEND" * 50, trade_id)
                    except:
                        pass
                    try:
                        trade_id = envelope["SetBiddingFail"]["BiddingFail"]["@TradeId"]
                        # #print(trade_id)
                        bidding_fail.trade_id = trade_id
                        # #print("TradeId", trade_id)
                    except:
                        pass
                    # Annulment
                    try:
                        trade_id = envelope["SetAnnulment"]["AnnulmentMessage"]["@TradeId"]
                        annulment.trade_id = trade_id
                        # #print("BiddingInvitationTradeID", trade_id)
                    except:
                        pass
                    try:
                        event_time = envelope["SetAnnulment"]["AnnulmentMessage"]["@EventTime"]
                        annulment.event_time = event_time
                        # #print("DebtorPersonEventTime", event_time)
                    except:
                        pass
                    try:
                        id_annulment = envelope["SetAnnulment"]["AnnulmentMessage"]["ID_Annulment"]
                        annulment.id_annulment = id_annulment
                        # #print("DebtorPersonEventTime", event_time)
                    except:
                        pass
                    try:
                        reason = envelope["SetAnnulment"]["AnnulmentMessage"]["Reason"]
                        annulment.reason = reason
                        # #print("DebtorPersonEventTime", event_time)
                    except:
                        pass
                    #
                    try:
                        trade_id = envelope["SetBiddingResult"]["BiddingResult"]["@TradeId"]
                        bidding_result.trade_id = trade_id
                        # #print('tradeid', trade_id)
                    except:
                        pass
                    try:
                        trade_id = envelope["SetBiddingStart"]["BiddingStart"]["@TradeId"]
                        bidding_start.trade_id = trade_id
                        # #print('tradeid', trade_id)
                    except:
                        pass
                    try:
                        trade_id = envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                            "@TradeId"]
                        application_session_statistic.trade_id = trade_id
                        # #print('tradeid', trade_id)
                    except:
                        pass
                    try:
                        trade_id = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"][
                            "@TradeId"]
                        bidding_proccess_info.trade_id = trade_id
                        # #print("TradeId", trade_id)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"][
                            "@EventTime"]
                        bidding_proccess_info.event_time = event_time
                        # #print("EventTime", event_time)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingCancel"]["BiddingCancel"][
                            "@EventTime"]
                        bidding_cancel.event_time = event_time
                        # #print("EventTime", event_time)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingEnd"]["BiddingEnd"][
                            "@EventTime"]
                        bidding_end.event_time = event_time
                        # #print("EventTime", event_time)
                    except:
                        pass
                    try:
                        event_time = envelope["SetApplicationSessionEnd"]["ApplicationSessionEnd"][
                            "@EventTime"]
                        application_session_end.event_time = event_time
                        # #print("eventtimeEnd", event_time2)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingFail"]["BiddingFail"][
                            "@EventTime"]
                        bidding_fail.event_time = event_time
                        # #print("EventTime", event_time)
                    except:
                        pass
                    try:
                        lot_number = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"]["PriceInfo"][
                            "@LotNumber"]
                        price_info.lot_number = lot_number
                        # #print("LotNumber", lot_number)
                    except:
                        pass
                    try:
                        lot_number = envelope["SetApplicationSessionEnd"]["ApplicationSessionEnd"][
                            "LotList"]["LotInfo"]["@LotNumber"]
                        lot_info.lot_number = lot_number
                        # #print("eventtimeEnd", event_time2)
                    except:
                        pass
                    try:
                        reason = envelope["SetBiddingCancel"]["BiddingCancel"]["@Reason"]
                        # #print("Reason", reason)
                        bidding_cancel.reason = reason

                    except:
                        pass
                    try:
                        reason = envelope["SetBiddingFail"]["BiddingFail"]["@Reason"]
                        # #print("Reason", reason)
                        bidding_fail.reason = reason

                    except:
                        pass
                    try:
                        reason = envelope["SetBiddingFail"]["BiddingFail"]["LotList"]["BiddingStateLotInfo"]["@Reason"]
                        # #print("Reason", reason)
                        bidding_fail.reason = reason

                    except:
                        pass
                    try:
                        new_price = envelope["SetBiddingProcessInfo"]["BiddingProcessInfo"]["PriceInfo"][
                            "@NewPrice"]
                        price_info.new_price = new_price
                        # #print("NewPrice", new_price)
                    except:
                        pass
                    try:
                        event_time1 = envelope["SetBiddingProcessInfo"]["BiddingProccesInfo"]["@EventTime"]
                        bidding_proccess_info.event_time = event_time1
                        # #print("eventtimeProccesInfo", event_time1)
                    except:
                        pass
                    try:
                        event_time = envelope["SetApplicationSessionEnd"]["ApplicationSessionEnd"][
                            "@EventTime"]
                        application_session_end.event_time = event_time
                        # #print("eventtimeEnd", event_time2)
                    except:
                        pass
                    try:
                        event_time = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "@EventTime"]
                        application_session_statistic.event_time = event_time
                        # #print("eventtimeStat", event_time)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingResult"]["BiddingResult"]["@EventTime"]
                        bidding_result.event_time = event_time
                        # #print('eventtime', event_time)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingStart"]["BiddingStart"]["@EventTime"]
                        bidding_start.event_time = event_time
                        # #print('eventtime', event_time)
                    except:
                        pass
                    try:
                        event_time = envelope["SetBiddingEnd"]["BiddingEnd"]["@EventTime"]
                        bidding_end.event_time = event_time
                        # #print('eventtime', event_time)
                    except:
                        pass
                    try:
                        lot_number = envelope["SetBiddingEnd"]["BiddingEnd"]["LotList"]["LotInfo"][
                            "@LotNumber"]
                        lot_info.lot_number = lot_number
                        # #print('eventtime', lot_number)
                    except:
                        pass
                    try:
                        date_begin = envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                            "DateBegin"]

                        application_session_statistic.date_begin = date_begin
                        # #print("DateBegin", date_begin)
                    except:
                        pass
                    try:
                        lot_number = \
                            envelope["SetApplicationSessionEnd"]["ApplicationSessionEnd"]["LotList"][
                                "LotInfo"][
                                "@LotNumber"]
                        lot_info.lot_number = lot_number

                        # #print("LotNumber", lot_number)
                    except:
                        pass
                    try:
                        lot_number = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "LotList"]["LotStatistic"][
                                "@LotNumber"]
                        lot_statistic.lot_number = lot_number
                        # #print("LotNumber", lot_number)
                    except:
                        pass
                    try:
                        lot_number = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"][
                                "@LotNumber"]
                        lot_trade_result.lot_number = lot_number
                        # #print("LotNumber", lot_number)
                    except:
                        pass
                    try:
                        substantiation = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"][
                                "FailureTradeResult"]["Substantiation"]
                        failure_trade_result.substantiation = substantiation
                        #print(failure_trade_result)

                        # #print("substantiation", substantiation)
                    except Exception as ex:
                        pass

                        #print("SUB" * 50)

                    try:
                        substantiation = \
                            envelope["ns1:SetBiddingResult"]["ns1:BiddingResult"][
                                "ns1:LotList"]["ns1:LotTradeResult"][
                                "ns1:FailureTradeResult"]["ns1:Substantiation"]
                        failure_trade_result.substantiation = substantiation

                        # #print("substantiation", substantiation)
                    except:
                        pass
                    try:
                        price = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"][
                                "FailureTradeResult"]["Price"]
                        failure_trade_result.price = price

                        # #print("price", price)
                    except:
                        pass
                    try:
                        participants = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"][
                                "Participants"]
                        lot_trade_result.participants = participants

                        # #print("Participants", participants)
                    except:
                        pass
                    try:
                        price = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "@Price"]
                        success_trade_result.price = price
                        # #print("Price", price)
                    except:
                        pass
                    # winnerCompany
                    try:
                        full_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@FullName"]
                        winner_company.full_name = full_name
                    except:
                        pass

                    try:
                        short_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@ShortName"]
                        winner_company.short_name = short_name
                        # #print("ShortName", short_name)
                    except:
                        pass
                    try:
                        inn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@INN"]
                        winner_company.inn = inn
                        # #print("INN", inn)
                    except:
                        pass
                    try:
                        ogrn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@OGRN"]
                        winner_company.ogrn = ogrn
                        # #print("OGRN", ogrn)
                    except:
                        pass
                    try:
                        legal_address = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@LegalAddress"]
                        winner_company.legal_address = legal_address
                        # #print("LegalAddress", legal_address)
                    except:
                        pass
                    try:
                        phone = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@Phone"]
                        winner_company.phone = phone
                        # #print("Phone", phone)
                    except:
                        pass
                    try:
                        post_address = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@PostAddress"]
                        winner_company.post_address = post_address
                        # #print("PostAddress", post_address)
                    except:
                        pass
                    try:
                        email = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerCompany"]["@Email"]
                        winner_company.email = email
                        # #print("LegalAddress", email)
                    except:
                        pass
                    # if winner_person.first_name is not None:
                    #     winner_person.save()
                    # if winner_company.full_name is not None:
                    #     winner_company.save()
                    try:
                        substantiation = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"][
                                "SuccessTradeResult"]["Substantiation"]
                        success_trade_result.substantiation = substantiation

                        # #print("substantiation", substantiation)
                    except:
                        pass
                    try:
                        substantiation = \
                            envelope["ns1:SetBiddingResult"]["ns1:BiddingResult"][
                                "ns1:LotList"]["ns1:LotTradeResult"][
                                "ns1:SuccessTradeResult"]["Substantiation"]
                        success_trade_result.substantiation = substantiation

                        # #print("substantiation", substantiation)
                    except:
                        pass

                    try:
                        price = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"][
                                "SuccessTradeResult"]["@Price"]
                        success_trade_result.price = price

                        # #print("price", price)
                    except:
                        pass
                    try:
                        price = \
                            envelope["ns1:SetBiddingResult"]["ns1:BiddingResult"][
                                "ns1:LotList"]["ns1:LotTradeResult"][
                                "ns1:SuccessTradeResult"]["@Price"]
                        success_trade_result.price = price

                        # #print("price", price)
                    except:
                        pass
                    # try:
                    #     if success_trade_result.price is not None:
                    #         success_trade_result.winner_company = winner_company
                    #         success_trade_result.winner_person = winner_person
                    #         success_trade_result.save()
                    # except Exception as ex:
                    #     #pass
                    #     ##print("tradres")
                    #     sleep(5)
                    # WinnerCompanyEnd
                    ##ParticipantPerson

                    # #print("Participant", i)
                    try:
                        first_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantPerson'][
                                "@FirstName"]
                        participant_person.first_name = first_name

                        # #print(first_name)

                    except:
                        pass

                    try:
                        last_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantPerson'][
                                "@LastName"]
                        participant_person.last_name = last_name
                        # #print(last_name)
                    except:
                        pass
                    try:
                        middle_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantPerson'][
                                "@MiddleName"]
                        participant_person.middle_name = middle_name
                        # #print(middle_name)
                    except:
                        pass
                    try:
                        inn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantPerson'][
                                "@INN"]
                        participant_person.inn = inn
                        # #print(inn)
                    except:
                        pass
                    try:
                        address = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantPerson'][
                                "@Address"]
                        participant_person.address = address
                        # #print(address)
                    except:
                        pass
                    try:
                        phone = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantPerson'][
                                "@Phone"]
                        participant_person.phone = phone
                        # #print(phone)
                    except:
                        pass
                    try:
                        email = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantPerson'][
                                "@Email"]
                        participant_person.email = email
                        # #print(email)
                    except:
                        pass
                    ##_
                    # participantCompany
                    try:
                        full_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantCompany']["@FullName"]
                        participant_company.full_name = full_name
                        #print(full_name)
                        #print("F" * 50)
                        # #print(first_name)

                    except:
                        pass

                    try:
                        short_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantCompany'][
                                "@ShortName"]
                        participant_company.short_name = short_name
                        # #print(last_name)
                    except:
                        pass
                    try:
                        inn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantCompany'][
                                "@INN"]
                        participant_company.inn = inn
                        # #print(middle_name)
                    except:
                        pass
                    try:
                        ogrn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantCompany'][
                                "@OGRN"]
                        participant_company.ogrn = ogrn
                        # #print(inn)
                    except:
                        pass
                    try:
                        legal_address = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantCompany'][
                                "@LegalAddress"]
                        participant_company.legal_address = legal_address
                        # #print(address)
                    except:
                        pass
                    try:
                        post_address = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantCompany'][
                                "@PostAddress"]
                        participant_company.post_address = post_address
                        # #print(phone)
                    except:
                        pass
                    try:
                        phone = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantCompany'][
                                "@Phone"]
                        participant_company.phone = phone
                        # #print(phone)
                    except:
                        pass
                    try:
                        email = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"][
                                'ParticipantCompany'][
                                "@Email"]
                        participant_company.email = email
                        # #print(email)
                    except:
                        pass
                    ###########################
                    try:
                        first_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerPerson"]["@FirstName"]
                        buyer_person.first_name = first_name
                        # buyer_company.save()
                        # #print("BuyerCompany FullName", full_name)
                    except:
                        pass
                    try:
                        middle_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerPerson"]["@MiddleName"]
                        buyer_person.middle_name = middle_name
                        # #print("ShortName", short_name)
                    except:
                        pass
                    try:
                        last_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerPerson"]["@LastName"]
                        buyer_person.last_name = last_name
                        # #print("ShortName", short_name)
                    except:
                        pass
                    try:
                        inn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerPerson"]["@INN"]
                        buyer_person.inn = inn
                        # #print("INN", inn)
                    except:
                        pass

                    try:
                        address = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerPerson"]["@Address"]
                        buyer_person.address = address
                        # #print("OGRN", ogrn)
                    except:
                        pass
                    ##
                    try:
                        full_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerCompany"]["@FullName"]
                        buyer_company.full_name = full_name
                        # buyer_company.save()
                        # #print("BuyerCompany FullName", full_name)
                    except:
                        pass
                    try:
                        short_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerCompany"]["@ShortName"]
                        buyer_company.short_name = short_name
                        # #print("ShortName", short_name)
                    except:
                        pass
                    try:
                        inn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerCompany"]["@INN"]
                        buyer_company.inn = inn
                        # #print("INN", inn)
                    except:
                        pass
                    try:
                        nil = \
                            envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"][
                                "ns1:LotList"][
                                "ns1:Lot"][
                                "ns1:StepPrice"]["@xsi:nil"]
                        step_price_model.nil = json.loads(nil)

                    except:
                        pass
                    try:
                        nil = \
                            envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["LotList"][
                                "Lot"][
                                "StepPrice"]["@xsi:nil"]
                        step_price_model.nil = json.loads(nil)

                    except:
                        pass
                    try:
                        ogrn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerCompany"]["@OGRN"]
                        buyer_company.ogrn = ogrn
                        # #print("OGRN", ogrn)
                    except:
                        pass
                    try:
                        legal_address = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['FailureTradeResult'][
                                "BuyerCompany"]["@LegalAddress"]
                        buyer_company.legal_address = legal_address
                        # #print("OGRN", ogrn)
                    except:
                        pass

                    # #TradeOrganizer
                    # try:
                    #     first_name = \
                    #         envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                    #             "TradeOrganizerPerson"][
                    #             "@FirstName"]
                    #     trade_organizer_person.first_name = first_name
                    #     ##print("TradeOrganizerFirstName", first_name)
                    # except:
                    #     pass
                    # try:
                    #     last_name = \
                    #         envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                    #             "TradeOrganizerPerson"][
                    #             "@LastName"]
                    #     trade_organizer_person.last_name = last_name
                    #     ##print("TradeOrganizerLastName", last_name)
                    # except:
                    #     pass
                    # try:
                    #     middle_name = \
                    #         envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                    #             "TradeOrganizerPerson"][
                    #             "@MiddleName"]
                    #     trade_organizer_person.middle_name = middle_name
                    #     ##print("TradeOrganizerMiddleName", middle_name)
                    # except:
                    #     pass
                    # try:
                    #     inn = \
                    #         envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                    #             "TradeOrganizerPerson"][
                    #             "@INN"]
                    #     trade_organizer_person.inn = inn
                    #     ##print("TradeOrganizerINN", inn)
                    # except:
                    #     pass
                    # try:
                    #     snils = \
                    #         envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeOrganizer"][
                    #             "TradeOrganizerPerson"][
                    #             "@SNILS"]
                    #     trade_organizer_person.snils = snils
                    #     ##print("TradeOrganizerSnils", snils)
                    # except:
                    #     pass
                    # #_________
                    try:
                        full_name = \
                            envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                                "ns1:DebtorCompany"][
                                "@FullName"]
                        debtor_company.full_name = full_name

                        # #print("DebtorCompanyFullName", full_name)
                    except:
                        pass
                    try:
                        short_name = \
                            envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                                "ns1:DebtorPerson"][
                                "@ShortName"]
                        debtor_company.short_name = short_name
                        # #print("DebtorCompanyShortName", short_name)
                    except:
                        pass

                    try:
                        inn = \
                            envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                                "ns1:DebtorCompany"][
                                "@INN"]
                        debtor_company.inn = inn
                        # #print("DebtorPersonINN", inn)
                    except:
                        pass
                    try:
                        ogrn = \
                            envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                                "ns1:DebtorCompany"][
                                "@OGRN"]
                        debtor_company.ogrn = ogrn
                        # #print("DebtorOGRN", ogrn)
                    except:
                        pass

                    try:
                        first_name = \
                            envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                                "ns1:DebtorPerson"][
                                "@FirstName"]
                        debtor_person.first_name = first_name
                        # #print("DebtorPersonFirsName", first_name)
                        # sleep()
                    except:
                        pass
                    try:
                        last_name = \
                            envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                                "ns1:DebtorPerson"][
                                "@LastName"]
                        debtor_person.last_name = last_name
                        # #print("DebtorPersonLastName", last_name)
                    except:
                        pass
                    try:
                        middle_name = \
                            envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                                "ns1:DebtorPerson"][
                                "@MiddleName"]
                        debtor_person.middle_name = middle_name
                        # #print("DebtorPersonMiddleName", middle_name)
                    except:
                        pass
                    try:
                        inn = \
                            envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                                "ns1:DebtorPerson"][
                                "@INN"]
                        debtor_person.inn = inn
                        # #print("DebtorPersonINN", inn)
                    except:
                        pass
                    try:
                        snils = \
                            envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:Debtor"][
                                "ns1:DebtorPerson"][
                                "@SNILS"]
                        debtor_person.snils = snils
                        # #print("DebtorPersonSNILS", snils)

                    except:
                        pass
                    # Winner Person
                    try:
                        first_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["SuccessTradeResult"][
                                "WinnerPerson"]["@FirstName"]

                        winner_person.first_name = first_name
                        # winner_person.save()
                        # #print("FirstName--------------", first_name)
                    except KeyError as ex:
                        pass
                        # #print("except firstName")
                    try:
                        middle_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerPerson"]["@MiddleName"]
                        winner_person.middle_name = middle_name
                        # #print("MiddleName---------", middle_name)
                    except:
                        pass
                    try:
                        last_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerPerson"]["@LastName"]
                        winner_person.last_name = last_name
                        # #print("LastName------------", last_name)
                    except:
                        pass
                    try:
                        inn_person = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerPerson"]["@INN"]
                        winner_person.inn = inn_person
                        # #print("INN", inn_person)
                    except:
                        pass
                    try:
                        address = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerPerson"]["@Address"]
                        winner_person.address = address
                        # #print("Address", address)
                    except:
                        pass
                    try:
                        phone = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerPerson"]["@Phone"]
                        winner_person.phone = phone
                        # #print("Phone", phone)
                    except:
                        pass

                    try:
                        email = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerPerson"]["@Email"]
                        winner_person.email = email
                        # #print("Email", email)
                    except:
                        pass
                    try:
                        snils = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]['SuccessTradeResult'][
                                "WinnerPerson"]["@SNILS"]
                        winner_person.snils = snils
                        # #print("Email", email)
                    except:
                        pass
                    # #print("Winner")
                    try:
                        first_name = \
                            envelope["ns1:SetBiddingResult"]["ns1:BiddingResult"][
                                "ns1:LotList"]["ns1:LotTradeResult"]["ns1:SuccessTradeResult"][
                                "ns1:WinnerPerson"]["@FirstName"]

                        winner_person.first_name = first_name
                    except KeyError as ex:
                        pass
                        # #print("except firstName")
                    try:
                        middle_name = \
                            envelope["ns1:SetBiddingResult"]["ns1:BiddingResult"][
                                "ns1:LotList"]["ns1:LotTradeResult"]['ns1:SuccessTradeResult'][
                                "ns1:WinnerPerson"]["@MiddleName"]
                        winner_person.middle_name = middle_name
                        # #print("MiddleName---------", middle_name)
                    except:
                        pass
                    try:
                        last_name = \
                            envelope["ns1:SetBiddingResult"]["ns1:BiddingResult"][
                                "ns1:LotList"]["ns1:LotTradeResult"]['ns1:SuccessTradeResult'][
                                "ns1:WinnerPerson"]["@LastName"]
                        winner_person.last_name = last_name
                        # #print("LastName------------", last_name)
                    except:
                        pass
                    try:
                        inn_person = \
                            envelope["ns1:SetBiddingResult"]["ns1:BiddingResult"][
                                "ns1:LotList"]["ns1:LotTradeResult"]['ns1:SuccessTradeResult'][
                                "ns1:WinnerPerson"]["@INN"]
                        winner_person.inn = inn_person
                        # #print("INN", inn_person)
                    except:
                        pass
                    try:
                        address = \
                            envelope["ns1:SetBiddingResult"]["ns1:BiddingResult"][
                                "ns1:LotList"]["ns1:LotTradeResult"]['ns1:SuccessTradeResult'][
                                "ns1:WinnerPerson"]["@Address"]
                        winner_person.address = address
                        # #print("Address", address)
                    except:
                        pass
                    try:
                        phone = \
                            envelope["ns1:SetBiddingResult"]["ns1:BiddingResult"][
                                "ns1:LotList"]["ns1:LotTradeResult"]['ns1:SuccessTradeResult'][
                                "ns1:WinnerPerson"]["@Phone"]
                        winner_person.phone = phone
                        # #print("Phone", phone)
                    except:
                        pass
                    try:
                        time_result = \
                            envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"][
                                "ns1:CloseForm"][
                                "@TimeResult"]
                        close_form.time_result = time_result
                        # #print("TimeBegin", time_result)
                    except:
                        pass
                    try:
                        time_begin = \
                            envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["OpenForm"][
                                "@TimeBegin"]
                        open_form.time_begin = time_begin
                        # #print("TimeBegin", time_begin)
                    except:
                        pass
                    try:
                        time_result = \
                            envelope["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]["CloseForm"][
                                "@TimeResult"]
                        close_form.time_result = time_result
                        # #print("TimeBegin", time_result)
                    except:
                        pass

                    try:
                        time_end = \
                            envelope["ns1:SetBiddingInvitation"]["ns1:BiddingInvitation"]["ns1:TradeInfo"][
                                "ns1:OpenForm"][
                                "@TimeEnd"]
                        open_form.time_end = time_end
                        # #print("TimeBegin", time_end)
                    except:
                        pass
                    try:
                        email = \
                            envelope["ns1:SetBiddingResult"]["ns1:BiddingResult"][
                                "ns1:LotList"]["ns1:LotTradeResult"]['ns1:SuccessTradeResult'][
                                "ns1:WinnerPerson"]["@Email"]
                        winner_person.email = email
                        # #print("Email", email)
                    except:
                        pass
                    try:
                        snils = \
                            envelope["ns1:SetBiddingResult"]["ns1:BiddingResult"][
                                "ns1:LotList"]["ns1:LotTradeResult"]['ns1:SuccessTradeResult'][
                                "ns1:WinnerPerson"]["@SNILS"]
                        winner_person.snils = snils
                        # #print("Email", email)
                    except:
                        pass
                    try:
                        ogrnip = \
                            envelope["ns1:SetBiddingResult"]["ns1:BiddingResult"][
                                "ns1:LotList"]["ns1:LotTradeResult"]['ns1:SuccessTradeResult'][
                                "ns1:WinnerPerson"]["@OGRNIP"]
                        winner_person.ogrnip = ogrnip
                        # #print("Email", email)
                    except:
                        pass

                    # =================================================================winnerperson

                    try:
                        for i in range(len(
                                envelope["SetBiddingResult"]["BiddingResult"]["LotList"]["LotTradeResult"][
                                    "Participants"]["Participant"])):
                            # #print("Participant", i)
                            try:
                                first_name = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@FirstName"]
                                participant_person.first_name = first_name
                                # #print(first_name)

                            except:
                                pass

                            try:
                                last_name = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@LastName"]
                                participant_person.last_name = last_name
                                # #print(last_name)
                            except:
                                pass
                            try:
                                middle_name = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@MiddleName"]
                                participant_person.middle_name = middle_name
                                # #print(middle_name)
                            except:
                                pass
                            try:
                                inn = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@INN"]
                                participant_person.inn = inn
                                # #print(inn)
                            except:
                                pass
                            try:
                                address = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@Address"]
                                participant_person.address = address
                                # #print(address)
                            except:
                                pass
                            try:
                                phone = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@Phone"]
                                participant_person.phone = phone
                                # #print(phone)
                            except:
                                pass
                            try:
                                email = \
                                    envelope["SetBiddingResult"]["BiddingResult"][
                                        "LotList"]["LotTradeResult"]["Participants"]["Participant"][i][
                                        'ParticipantPerson'][
                                        "@Email"]
                                participant_person.email = email
                                # #print(email)
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
                        # #print(first_name)

                    except:
                        pass

                    try:
                        last_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"]['ParticipantPerson'][
                                "@LastName"]
                        participant_person.last_name = last_name
                        # #print(last_name)
                    except:
                        pass
                    try:
                        middle_name = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"]['ParticipantPerson'][
                                "@MiddleName"]
                        participant_person.middle_name = middle_name
                        # #print(middle_name)
                    except:
                        pass
                    try:
                        inn = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"]['ParticipantPerson'][
                                "@INN"]
                        participant_person.inn = inn
                        # #print(inn)
                    except:
                        pass
                    try:
                        address = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"]['ParticipantPerson'][
                                "@Address"]
                        participant_person.address = address
                        # #print(address)
                    except:
                        pass
                    try:
                        phone = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"]['ParticipantPerson'][
                                "@Phone"]
                        participant_person.phone = phone
                        # #print(phone)
                    except:
                        pass
                    try:
                        email = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "LotList"]["LotTradeResult"]["Participants"]["Participant"]['ParticipantPerson'][
                                "@Email"]
                        participant_person.email = email
                        # #print(email)
                    except:
                        pass
                    # _____________________________________________________-
                    try:
                        lot_number = envelope["SetBiddingFail"]["BiddingFail"][
                            "LotList"]["BiddingStateLotInfo"]["@LotNumber"]
                        # #print("LotNumber", lot_number)
                        bidding_state_lot_info.lot_number = lot_number

                    except:
                        pass
                    try:
                        reason = envelope["SetBiddingFail"]["BiddingFail"][
                            "LotList"]["BiddingStateLotInfo"]["@Reason"]
                        # #print("Reason", reason)
                        bidding_state_lot_info.reason = reason

                    except:
                        pass
                    try:
                        for lottraderesult in envelope["SetBiddingResult"]["BiddingResult"]["LotList"][
                            "LotTradeResult"]:
                            # ##print(j)
                            # for i in///// range(len(
                            #         envelope["soap:Body"]["SetBiddingResult"]["BiddingResult"]["LotList"]["LotTradeResult"][
                            #             "Participants"]["Participant"])):
                            # ##print("Participant", i)
                            try:
                                lot_number = lottraderesult["@LotNumber"]
                                lot_trade_result.lot_number = lot_number
                                # #print("LotNumber", lot_number)

                            except:
                                pass
                            try:
                                price = lottraderesult["SuccessTradeResult"]["@Price"]
                                success_trade_result.price = price
                                # #print("Price", price)

                            except:
                                pass
                            try:
                                price = lottraderesult["ns1:SuccessTradeResult"]["@Price"]
                                success_trade_result.price = price
                                # #print("Price", price)

                            except:
                                pass

                            try:

                                first_name = lottraderesult["SuccessTradeResult"]["WinnerPerson"]["@FirstName"]
                                winner_person.first_name = first_name
                                # winner_person.save()
                                # #print(first_name, "winner")


                            except:
                                pass

                            try:
                                last_name = \
                                    lottraderesult["SuccessTradeResult"]["WinnerPerson"][
                                        "@LastName"]
                                winner_person.last_name = last_name
                                # #print(last_name)
                            except:
                                pass
                            try:
                                middle_name = \
                                    lottraderesult["SuccessTradeResult"]["WinnerPerson"][
                                        "@MiddleName"]
                                winner_person.middle_name = middle_name
                                # #print(middle_name)
                            except:
                                pass
                            try:
                                inn = \
                                    lottraderesult["SuccessTradeResult"]["WinnerPerson"][
                                        "@INN"]
                                winner_person.inn = inn
                                # #print(inn)
                            except:
                                pass
                            try:
                                address = \
                                    lottraderesult["SuccessTradeResult"]["WinnerPerson"][
                                        "@Address"]
                                winner_person.address = address
                                # #print(address)
                            except:
                                pass
                            try:
                                phone = \
                                    lottraderesult["SuccessTradeResult"]["WinnerPerson"][
                                        "@Phone"]
                                winner_person.phone = phone
                                # #print(phone)
                            except:
                                pass
                            try:
                                email = \
                                    lottraderesult["SuccessTradeResult"]["WinnerPerson"][
                                        "@Email"]
                                winner_person.email = email
                                # #print(email)
                            except:
                                pass

                            # try:
                            #     if winner_person.first_name:
                            #         winner_person.save(zzz)
                            #         success_trade_result.winner_person = winner_person
                            #         #print("pre save")
                            #         #print(success_trade_result)
                            #         success_trade_result.save()
                            #         #print(success_trade_result.pk)
                            #         #print("after save")
                            #         #print(">"*50)
                            # except Exception as ex:
                            #     pass
                            #     #print("E"*50)
                            # try:
                            #     #print(lottraderesult["Participants"])
                            # except:
                            #     pass
                            try:

                                first_name = lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                    "ParticipantPerson"]["@FirstName"]
                                participant_person.first_name = first_name
                                # #print(first_name, "Participant ")

                            except:
                                pass

                            try:
                                last_name = \
                                    lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@LastName"]
                                participant_person.last_name = last_name
                                # #print(last_name)
                            except:
                                pass
                            try:
                                middle_name = \
                                    lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@MiddleName"]
                                participant_person.middle_name = middle_name
                                # #print(middle_name)
                            except:
                                pass
                            try:
                                inn = \
                                    lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@INN"]
                                participant_person.inn = inn
                                # #print(inn)
                            except:
                                pass
                            try:
                                address = \
                                    lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@Address"]
                                participant_person.address = address
                                # #print(address)
                            except:
                                pass
                            try:
                                phone = \
                                    lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@Phone"]
                                participant_person.phone = phone
                                # #print(phone)
                            except:
                                pass
                            try:
                                email = \
                                    lottraderesult["SuccessTradeResult"]["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@Email"]
                                participant_person.email = email
                                # #print(email)
                            except:
                                pass
                            # ===============================
                            try:

                                first_name = lottraderesult["Participants"]["Participant"][
                                    "ParticipantPerson"]["@FirstName"]
                                participant_person.first_name = first_name
                                # #print(first_name, "Participant ")

                            except:
                                pass

                            try:
                                last_name = \
                                    lottraderesult["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@LastName"]
                                participant_person.last_name = last_name
                                # #print(last_name)
                            except:
                                pass
                            try:
                                middle_name = \
                                    lottraderesult["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@MiddleName"]
                                participant_person.middle_name = middle_name
                                # #print(middle_name)
                            except:
                                pass
                            try:
                                inn = \
                                    lottraderesult["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@INN"]
                                participant_person.inn = inn
                                # #print(inn)
                            except:
                                pass
                            try:
                                address = \
                                    lottraderesult["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@Address"]
                                participant_person.address = address
                                # #print(address)
                            except:
                                pass
                            try:
                                phone = \
                                    lottraderesult["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@Phone"]
                                participant_person.phone = phone
                                # #print(phone)
                            except:
                                pass
                            try:
                                email = \
                                    lottraderesult["Participants"]["Participant"][
                                        "ParticipantPerson"][
                                        "@Email"]
                                participant_person.email = email
                                # #print(email)
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
                        # #print("accept_count", accept_count)
                    except:
                        pass
                    try:
                        entry_count = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "LotList"]["LotStatistic"][
                                "@EntryCount"]
                        lot_statistic.entry_count = entry_count
                        # #print("EntryCount", entry_count)
                    except:
                        pass
                    try:
                        result = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "LotList"]["LotStatistic"]["ApplicationList"]["ApplicationData"]["@Result"]
                        application_dataa.result = result

                        # #print("result", result)
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
                    #     ##print("result", result)
                    #
                    # except:
                    #     pass
                    try:
                        filename = envelope["SetBiddingInvitation"][
                            "BiddingInvitation"]["TradeInfo"]["Attach"]["FileName"]
                        attach.file_name = filename
                        #print(filename)
                        # #print("FileName", filename)

                    except Exception as ex:
                        pass

                    try:
                        Type = envelope["SetBiddingInvitation"][
                            "BiddingInvitation"]["TradeInfo"]["Attach"]["Type"]
                        attach.type = Type
                    except:
                        pass
                    try:
                        Blob = envelope["SetBiddingInvitation"][
                            "BiddingInvitation"]["TradeInfo"]["Attach"]["Blob"]
                        attach.blob = Blob
                    except:
                        pass
                    try:
                        filename = envelope["SetBiddingInvitation"][
                            "BiddingInvitation"]["Attach"]["FileName"]
                        attach.file_name = filename
                        # #print("FileName", filename)

                    except:
                        pass
                    try:
                        Type = envelope["SetBiddingInvitation"][
                            "BiddingInvitation"]["Attach"]["Type"]
                        attach.type = Type
                    except:
                        pass
                    try:
                        Blob = envelope["SetBiddingInvitation"][
                            "BiddingInvitation"]["Attach"]["Blob"]
                        attach.blob = Blob
                    except:
                        pass
                    try:
                        filename = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "Attach"]["FileName"]

                        attach.file_name = filename
                    except:
                        pass

                    try:
                        filename = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "Attach"]["FileName"]
                        # #print(envelope["SetBiddingResult"]["BiddingResult"])
                        attach.file_name = filename

                        # #print("filename", filename)
                    except:
                        pass
                    try:
                        filename = \
                            envelope["SetBiddingResult"]["BiddingResult"]["TradeInfo"][
                                "Attach"]["FileName"]
                        #print("filename", filename)
                        attach.file_name = filename

                        # #print("filename", filename)
                    except:
                        pass
                    try:
                        Type = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "Attach"]["Type"]
                        attach.type = Type

                        # #print("Type", Type)

                    except:
                        pass

                    try:
                        Type = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "Attach"]["Type"]
                        attach.type = Type

                        # #print("Type", Type)
                    except:
                        pass
                    try:
                        Type = \
                            envelope["SetBiddingResult"]["BiddingResult"]["TradeInfo"][
                                "Attach"]["Type"]
                        attach.type = Type

                        # #print("Type", Type)
                    except:
                        pass
                    try:
                        Blob = \
                            envelope["SetApplicationSessionStatistic"]["ApplicationSessionStatistic"][
                                "Attach"]["Blob"]
                        attach.blob = Blob
                        # attach.save()
                        # ##print("Blob", Blob)
                    except:
                        pass
                    try:
                        Blob = \
                            envelope["SetBiddingResult"]["BiddingResult"][
                                "Attach"]["Blob"]
                        attach.blob = Blob
                        # ##print("Blob", Blob)
                    except:
                        pass
                    try:
                        Blob = \
                            envelope["SetBiddingResult"]["BiddingResult"]["TradeInfo"][
                                "Attach"]["Blob"]
                        attach.blob = Blob
                        # ##print("Blob", Blob)
                    except:
                        pass
                    try:
                        filename = envelope["SetBiddingFail"][
                            "BiddingFail"]["Attach"]["FileName"]
                        attach.file_name = filename
                        # #print("FileName", filename)

                    except:
                        pass
                    try:
                        Type = envelope["SetBiddingFail"][
                            "BiddingFail"]["Attach"]["Type"]
                        attach.type = Type
                    except:
                        pass
                    try:
                        Blob = envelope["SetBiddingFail"][
                            "BiddingFail"]["Attach"]["Blob"]
                        attach.blob = Blob
                    except:
                        pass
                    try:
                        if buyer_person.first_name is not None:
                            buyer_person.save()
                    except:
                        pass
                    try:
                        if buyer_company.full_name is not None:
                            buyer_company.save()
                            #print(buyer_company)
                            #print(">" * 50)
                    except Exception as ex:
                        pass
                        #print(">" * 50)

                    try:
                        if success_trade_result.price is not None:
                            if winner_person.first_name is not None:
                                winner_person.save()
                                success_trade_result.winner_person = winner_person
                            if winner_company.full_name is not None:
                                winner_company.save()
                                success_trade_result.winner_company = winner_company
                            success_trade_result.save()
                    except:
                        pass
                    # #print("?"*50)
                    try:
                        if attach.file_name is not None:
                            attach.save()
                    except:
                        pass
                    try:
                        if failure_trade_result.substantiation is not None:
                            # failure_trade_result.buyer_company = buyer_company
                            failure_trade_result.save()
                    except Exception as ex:
                        pass
                        #print("SAVE" * 50)
                    try:
                        if application.time_begin is not None:
                            application.save()
                    except:
                        pass
                    try:
                        if participant_person.first_name is not None:
                            participant_person.save()
                            participant.participant_person = participant_person
                            participant.save()
                            participants_model.participant = participant
                            participants_model.save()

                    except:
                        pass
                    try:
                        if participant_company.full_name is not None:
                            participant_company.save()
                            participant.participant_company = participant_company
                            participant.save()
                            #print("0" * 50)
                            #print(type(participant))

                            participants_model.participant = participant
                            participants_model.save()
                    except Exception as ex:
                        pass
                        #print("$" * 50)
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
                        if debtor_person.first_name is not None:
                            debtor_person.save()
                            debtor.debtor_person = debtor_person
                            debtor.save()
                    except:
                        pass
                    try:
                        if step_price_model.nil is not None:
                            #print(step_price_model)
                            #print("<" * 50)
                            step_price_model.save()
                            lot.step_price = step_price_model
                    except Exception as ex:
                        pass
                        #print("<" * 50)
                    try:
                        if debtor_company.full_name is not None:
                            debtor_company.save()
                            debtor.debtor_company = debtor_company
                            debtor.save()
                    except:
                        pass
                    try:
                        if lot_info.lot_number is not None:
                            lot_info.save()
                            lot_list.lot_info = lot_info
                            lot_list.save()
                    except Exception as ex:
                        pass
                        #print("lotlist" * 60)
                    try:
                        if lot.lot_number:
                            lot.save()
                            lot_list.lot = lot
                            lot_list.save()
                    except:
                        pass
                    try:
                        if lot_trade_result.lot_number is not None:
                            if failure_trade_result.pk is not None:
                                lot_trade_result.failure_trade_result = failure_trade_result
                            if success_trade_result.pk is not None:
                                lot_trade_result.success_trade_result = success_trade_result
                            lot_trade_result.save()
                            lot_list.lot_trade_result = lot_trade_result
                            lot_list.save()
                    except:
                        pass
                    try:
                        if bidding_start.trade_id is not None:
                            # bidding_start.lot_list = lot_list
                            bidding_start.save()
                            set_bidding_start.bidding_start = bidding_start
                            set_bidding_start.save()
                            body.set_bidding_start = set_bidding_start
                    except:
                        pass
                    try:
                        if trade_info.auction_type is not None:
                            if attach.file_name is not None:
                                trade_info.attach = attach
                            trade_info.lot_list = lot_list
                            trade_info.save()
                    except:
                        pass
                    try:
                        if price_info.new_price is not None:
                            price_info.save()
                    except:
                        pass
                    try:
                        # lot_list.save()
                        if bidding_fail.trade_id:
                            # bidding_fail.lot_list = lot_list
                            if bidding_state_lot_info.lot_number is not None:
                                bidding_fail.lot_list = lot_list
                            bidding_fail.save()
                            set_bidding_fail.bidding_fail = bidding_fail
                            set_bidding_fail.save()
                            body.set_bidding_fail = set_bidding_fail


                    except:
                        pass
                    try:
                        if annulment.trade_id is not None:
                            annulment.save()
                            set_annulment.annulment_message = annulment
                            set_annulment.save()
                            body.set_annulment = set_annulment

                    except:
                        pass

                    # ##print(bidding_fail)
                    # ##print("create bidding fail in list")
                    # sleep(5)
                    # success_trade_result.save()

                    # #print("SUCCESSTRADE")
                    # sleep(5)
                    try:
                        if bidding_proccess_info.trade_id is not None:
                            bidding_proccess_info.price_info = price_info
                            bidding_proccess_info.save()
                            set_bidding_proccess_info.bidding_process_info = bidding_proccess_info
                            set_bidding_proccess_info.save()
                            body.set_bidding_proccess_info = set_bidding_proccess_info
                    except:
                        pass

                    try:
                        if bidding_result.trade_id is not None:

                            if lot_trade_result.lot_number is not None:
                                bidding_result.lot_list = lot_list
                            if attach.file_name is not None:
                                bidding_result.attach = attach
                            bidding_result.save()
                            set_bidding_result.bidding_result = bidding_result
                            set_bidding_result.save()
                            body.set_bidding_result = set_bidding_result
                    except:
                        pass

                    try:
                        if bidding_end.trade_id is not None:
                            if lot_info.lot_number is not None:
                                bidding_end.lot_list = lot_list
                            bidding_end.save()

                            set_bidding_end.bidding_end = bidding_end
                            set_bidding_end.save()
                            body.set_bidding_end = set_bidding_end
                    except:
                        pass
                    try:
                        if bidding_cancel.trade_id is not None:
                            # bidding_cancel.lot_list = lot_list
                            bidding_cancel.save()
                            set_bidding_cancel.bidding_cancel = bidding_cancel
                            set_bidding_cancel.save()
                            body.set_bidding_cancel = set_bidding_cancel
                    except:
                        pass
                    try:
                        if bidding_state_lot_info.lot_number is not None:
                            bidding_state_lot_info.save()
                    except:
                        pass
                    try:
                        if application_session_start.trade_id is not None:
                            if lot_info.lot_number is not None:
                                application_session_start.lot_list = lot_list
                            application_session_start.save()
                            set_application_session_start.application_session_start = application_session_start
                            set_application_session_start.save()
                            body.set_application_session_start = set_application_session_start


                    except:
                        pass

                    if application_session_end.trade_id is not None:
                        # lot_list.save()
                        if lot_info.lot_number is not None:
                            application_session_end.lot_list = lot_list
                        application_session_end.save()
                        set_application_session_end.application_session_end = application_session_end
                        set_application_session_end.save()
                        body.set_application_session_end = set_application_session_end
                    try:
                        if lot_statistic.lot_number is not None:
                            lot_statistic.save()
                            lot_list.lot_statistic = lot_statistic
                            lot_list.save()
                    except:
                        pass
                    try:
                        if application_session_statistic.trade_id is not None:
                            if lot_statistic.lot_number is not None:
                                application_session_statistic.lot_list = lot_list
                            application_session_statistic.attach = attach
                            application_session_statistic.save()
                            set_application_session_statistic.application_session_statistic = application_session_statistic
                            set_application_session_statistic.save()
                            body.set_application_session_statistic = set_application_session_statistic


                    except:
                        pass
                        # #print( "in LIST")
                        # sleep(5
                        # )
                        # #print("^" * 50)

                        # body.set_bidding_proccess_info = set_bidding_proccess_info
                        # body.set_bidding_fail = set_bidding_fail
                        # body.set_bidding_end = set_bidding_end
                        # body.set_bidding_cancel = set_bidding_cancel
                        # try:
                        #     body.set_application_session_start = set_application_session_start
                        # except:
                        #     pass
                        # try:
                        #     # body.set_application_session_end = set_application_session_end
                        # except:
                        pass
                    # try:
                    #     body.set_application_session_statistic = set_application_session_statistic
                    # except:
                    #     pass
                    #print("*" * 50)
                    #print(body)
                    body.save()
                    #print(body)

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

                    trade_place.trade_list = trade_list
                    trade_list.save()
                    trade_place.save()
                    trade_place_list.trade_place = trade_place
                    trade_place_list.save()


        except Exception as ex:
            pass
            #print('From list')
        # #print("END OF")
        # sleep(5)

    # for msg_data in data_json["MessageList"]["MessageData"]:
    #     #print(msg_data,"0 dc")


    try:
        for msg_data in data_json["MessageList"]["MessageData"]:
            try:
                status = ''
                message_data = MessageData()
                publisher = Publisher()
                fio = Fio()
                sro = Sro()
                publisher_arbitr_manager_v2 = Publisher_Arbitr_Manager_v2()
                publisher_arbitr_manager_sro_v2 = Publisher_Arbitr_Manager_Sro_v2()
                publisher_firmtrade_organizer_v2 = Publisher_FirmTrade_Organizer_v2()
                publisher_persontrade_organizer_v2 = Publisher_PersonTrade_Organizer_v2()
                publisher_company_v2 = Publisher_Company_v2()
                publisher_person_v2 = Publisher_Person_v2()
                publisher_centralbankrf_v2 = Publisher_CentralBankRf_v2()
                publisher_asv_v2 = Publisher_Asv_v2()
                publisher_fnsdepartment_v2 = Publisher_FnsDepartment_v2()
                publisher_efrsb_v2 = Publisher_Efrsb_v2()
                publisher_mfc_v2 = Publisher_Mfc_v2()
                court_decision = CourtDecision()
                sale_contract_result2 = SaleContractResult2()
                message_info = MessageInfo()
                contracts = Contracts()
                decision_type = DecisionType()
                court_decree = CourtDecree()
                arbitr_manager_info = ArbitrManagerInfo()
                legal_case_termination_type = LegalCaseTerminationType()
                procedure_prolongation = ProcedureProlongation()
                cancelled_message = CanceledMessages()
                auction = Auction()
                application = Application()
                lot_table = LotTable()
                auction_lot = AuctionLot()
                sale_contract_info = SaleContractInfo()
                auction_lot_classifier = AuctionLotClassifier()
                meeting = Meeting()
                meeting_result = MeetingResult()
                trade_result = TradeResult()
                trade_result_lot = TradeResultLot()
                winner = Winner()
                buyer = Buyer()
                participant_company = ParticipantCompany()
                participant_person = ParticipantPerson()
                appoint_administration = AppointAdministration()
                other = Other()
                director = Director()
                change_administration = ChangeAdministration()
                termination_administration = TerminationAdministraion()
                begin_executory_process = BeginExecutoryProcess()
                transfer_assert_for_implementation = TransferAssertsForImplementation()
                annul = Annul()
                property_inventory_result = PropertyInventoryResult()
                property_evaluation_report = PropertyEvaluationReport()
                sale_contract_result = SaleContractResult()
                failure_winner_info = FailureWinnerInfo()
                purchaser_info = PurchaserInfo()
                committee = Committee()
                sale_order_pledged_property = SaleOrderPledgedProperty()
                receiving_creditor_demand = ReceivingCreditorDemand()
                deliberate_bankruptcy = DeliberateBankruptcy()
                intention_credit_org = IntentionCreditOrg()
                liabilities_credit_org = LiabilitiesCreditOrg()
                perfomance_credit_org = PerformanceCreditOrg()
                buying_property = BuyingProperty()
                declaration_person_damages = DeclarationPersonDamages()
                bankrupt_supervisory_persons = BankruptSupervisoryPersons()
                bankrupt_supervisory_person = BankruptSupervisoryPerson()
                another_person_for_responsibility = AnotherPersonsForResponsibility()
                person_for_responsibility = PersonForResponsibility()
                act_person_damages = ActPersonDamages()
                act_review_person_damages = ActReviewPersonDamages()
                deal_invalid = DealInvalid()
                deal_participants = DealParticipants()
                deal_participant = DealParticipant()
                act_deal_invalid = ActDealInvalid()
                act_deal_invalid2 = ActDealInvalid2()
                deal_info = DealInfo()
                deals = Deals()
                act_review_deal_invalid = ActReviewDealInvalid()
                act_review_deal_invalid2 = ActReviewDealInvalid2()
                acts = Acts()
                act_info = ActInfo()
                declaration_person_subsidiary = DeclarationPersonSubsidiary()
                act_person_subsidiary = ActPersonSubsidiary()
                act_review_person_subsidiary = ActReviewPersonSubsidiary()
                meeting_worker = MeetingWorker()
                meeting_worker_result = MeetingWorkerResult()
                view_draft_restructuring_plan = ViewDraftRestructuringPlan()
                view_exec_restructuring_plan = ViewExecRestructuringPlan()
                transfer_ownership_real_estate = TransferOwnershipRealEstate()
                land_plots = LandPlots()
                land_plot = LandPlot()
                uncompleted_building_projects = UncompletedBuildingProjects()
                uncompleted_building_project = UncompletedBuildingProject()
                cancel_auction_trade_result = CancelAuctionTradeResult()
                cancel_deliberate_bankruptcy = CancelDeliberateBankruptcy()
                change_deliberate_bankruptcy = ChangeDeliberateBankruptcy()
                reducing_size_share_capital = ReducingSizeShareCapital()
                selection_purchaser_assets = SelectionPurchaserAssets()
                estimates_current_expenses = EstimatesCurrentExpenses()
                order_and_timing_calculations = OrderAndTimingCalculations()
                information_about_bankruptcy = InformationAboutBankruptcy()
                estimates_and_unsold_assets = EstimatesAndUnsoldAssets()
                remaining_assets_and_right = RemainingAssetsAndRight()
                impending_transfer_assets = ImpendingTransferAssets()
                credit_organizations = CreditOrganizations()

                credit_organization_info = CreditOrganizationInfo()
                transfer_assets = TransferAssets()
                transfer_insurance_portfolio = TransferInsurancePortfolio()
                insurance_organization = InsuranceOrganization()
                bank_open_account_debtor = BankOpenAccountDebtor()
                procedure_granting_indemnity = ProcedureGrantingIndemnity()
                right_unsold_asset = RightUnsoldAsset()
                transfer_responsibilities_fund = TransferResponsibilitiesFund()
                extension_administration = ExtensionAdministration()
                meeting_participants_building = MeetingParticipantsBuilding()
                meeting_part_build_result = MeetingPartBuildResult()
                part_build_monetary_claim = PartBuildMonetaryClaim()
                start_settlement = StartSettlement()
                process_inventory_debtor = ProcessInventoryDebtor()
                rebuttal = Rebuttal()
                creditor_choice_right_subsidiary = CreditorChoiceRightSubsidiary()
                accession_declaration_subsidiary = AccessionDeclarationSubsidiary()
                disqualification_arbitration_manager = DisqualificationArbitrationManager()
                disqualification_arbitration_manager2 = DisqualificationArbitrationManager2()
                court = Court()
                duration = Duration()
                change_estimates_current_expenses = ChangeEstimatesCurrentExpenses()
                act_person_subsidiary2 = ActPersonSubsidiary2()
                declaration_person_subsidiary_info_messages = DeclarationPersonSubsidiaryInfoMessages()
                act_review_person_subsidiary2 = ActReviewPersonSubsidiary2()
                act_person_subsidiary_info_messages = ActPersonSubsidiaryInfoMessages()
                assessment_report = AssessmentReport()
                appraisers = Appraisers()
                appraiser = Appraiser()

                object_of_assessment = ObjectOfAssessment()
                objects_of_assessments = ObjectOfAssessment()
                report = Report()
                classifier = Classifier()
                expert = Expert()
                experts = Experts()
                expert_decision = ExpertDecision()
                return_of_application_on_extrajudicial_bankruptcy = ReturnOfApplicationOnExtrajudicialBankruptcy()
                start_of_extrajudicial_bankruptcy = StartOfExtrajudicialBankruptcy()
                creditors_non_from_entrepreneurship = CreditorsNonFromEntrepreneurship()
                creditors_from_entrepreneurship = CreditorsFromEntrepreneurship()
                banks = Banks()
                bank = Bank()
                monetary_obligations = MonetaryObligations()
                monetary_obligation = MonetaryObligation()
                arbitr_manager = ArbitrManager()
                message = Message()
                obligatory_payment = ObligatoryPayment()
                obligatory_payments = ObligatoryPayments()
                termination_of_extrajudicial_bankruptcy = TerminationOfExtrajudicialBankruptcy()
                completion_of_extrajudicial_bankruptcy = CompletionOfExtrajudicialBankruptcy()
                bankrupt_company_v2 = Bankrupt_Company_v2()
                bankrupt_person_v2 = Bankrupt_Person_v2()
                category = Category()
                fio_history = FioHistory()
                file_info = FileInfo()
                file_info_list = FileInfoList()
                message_url = MessageUrl()
                bankrupt_info = BankruptInfo()
                bankrupt = Bankrupt()
                change_auction = ChangeAuction()
                message_types = MessageTypes()
                # classifier_collection = Classifi
                # #print(msg_data.keys())
                # #print(msg_data["Id"])
                #print(msg_data)
                try:
                    message_data.id_message_data = msg_data["Id"]
                except:
                    pass
                try:
                    message_data.number = msg_data["Number"]
                except:
                    pass
                try:
                    message_data.case_number = msg_data["CaseNumber"]
                except Exception as ex:
                    pass
                    #print("ex"*50)

                xsi_type = msg_data["Publisher"]["@xsi:type"]
                #print(xsi_type)
                if xsi_type == "Publisher.ArbitrManager.v2":
                    try:
                        publisher_arbitr_manager_v2.inn = msg_data["Publisher"]["Inn"]
                    except:
                        pass
                    try:
                        publisher_arbitr_manager_v2.snils = msg_data["Publisher"]["Snils"]
                    except:
                        pass
                    try:
                        publisher_arbitr_manager_v2.ogrnip = msg_data["Publisher"]["Ogrnip"]
                    except:
                        pass
                    try:
                        publisher_arbitr_manager_v2.correspondence_address = msg_data["Publisher"]["CorrespondenceAddress"]
                    except:
                        pass
                    try:
                        sro.name = msg_data["Publisher"]["Sro"]["Name"]
                    except:
                        pass
                    try:
                        sro.ogrn = msg_data["Publisher"]["Sro"]["Ogrn"]
                    except:
                        pass
                    try:
                        sro.inn = msg_data["Publisher"]["Sro"]["Inn"]
                    except:
                        pass
                    try:
                        sro.address = msg_data["Publisher"]["Sro"]["Address"]
                    except:
                        pass
                    try:
                        fio.last_name = msg_data["Publisher"]["Fio"]["LastName"]
                    except:
                        pass
                    try:
                        fio.first_name = msg_data["Publisher"]["Fio"]["FirstName"]
                    except:
                        pass
                    try:
                        fio.middle_name = msg_data["Publisher"]["Fio"]["MiddleName"]
                    except:
                        pass

                if xsi_type == "Publisher.ArbitrManagerSro.v2":
                    try:
                        publisher_arbitr_manager_sro_v2.name = msg_data["Publisher"]["Name"]
                    except Exception as ex:
                        #print("#"*50)
                        pass
                    try:
                        publisher_arbitr_manager_sro_v2.ogrn = msg_data["Publisher"]["Ogrn"]
                    except:
                        pass
                    try:
                        publisher_arbitr_manager_sro_v2.inn = msg_data["Publisher"]["Inn"]
                    except:
                        pass
                    try:
                        publisher_arbitr_manager_sro_v2.address = msg_data["Publisher"]["Address"]
                    except:
                        pass
                    #fio
                    try:
                        fio.last_name = msg_data["Publisher"]["Fio"]["LastName"]
                    except:
                        pass
                    try:
                        fio.first_name = msg_data["Publisher"]["Fio"]["FirstName"]
                    except:
                        pass
                    try:
                        fio.middle_name = msg_data["Publisher"]["Fio"]["MiddleName"]
                    except:
                        pass
                    #sro
                    try:
                        sro.name = msg_data["Publisher"]["Sro"]["Name"]
                    except:
                        pass
                    try:
                        sro.ogrn = msg_data["Publisher"]["Sro"]["Ogrn"]
                    except:
                        pass
                    try:
                        sro.inn = msg_data["Publisher"]["Sro"]["Inn"]
                    except:
                        pass
                    try:
                        sro.address = msg_data["Publisher"]["Sro"]["Address"]
                    except:
                        pass


                if xsi_type == "Publisher.FirmTradeOrganizer.v2":
                    try:
                        publisher_firmtrade_organizer_v2.name = msg_data["Publisher"]["Name"]
                    except:
                        pass
                    try:
                        publisher_firmtrade_organizer_v2.ogrn = msg_data["Publisher"]["Ogrn"]
                    except:
                        pass
                    try:
                        publisher_firmtrade_organizer_v2.inn = msg_data["Publisher"]["Inn"]
                    except:
                        pass

                if xsi_type == "Publisher.PersonTradeOrganizer.v2":
                    try:
                        publisher_persontrade_organizer_v2.inn = msg_data["Publisher"]["Inn"]
                    except:
                        pass
                    try:
                        publisher_persontrade_organizer_v2.ogrnip = msg_data["Publisher"]["Ogrnip"]
                    except:
                        pass
                    try:
                        fio.last_name = msg_data["Publisher"]["Fio"]["LastName"]
                    except:
                        pass
                    try:
                        fio.first_name = msg_data["Publisher"]["Fio"]["FirstName"]
                    except:
                        pass
                    try:
                        fio.middle_name = msg_data["Publisher"]["Fio"]["MiddleName"]
                    except:
                        pass


                if xsi_type == "Publisher.Company.v2":
                    try:
                        publisher_company_v2.name = msg_data["Publisher"]["Name"]
                    except:
                        pass
                    try:
                        publisher_company_v2.ogrn = msg_data["Publisher"]["Ogrn"]
                    except:
                        pass
                    try:
                        publisher_company_v2.inn = msg_data["Publisher"]["Inn"]
                    except:
                        pass

                if xsi_type == "Publisher.Person.v2":
                    try:
                        publisher_person_v2.inn = msg_data["Publisher"]["Inn"]
                    except:
                        pass
                    try:
                        fio.last_name = msg_data["Publisher"]["Fio"]["LastName"]
                    except:
                        pass
                    try:
                        fio.first_name = msg_data["Publisher"]["Fio"]["FirstName"]
                    except:
                        pass
                    try:
                        fio.middle_name = msg_data["Publisher"]["Fio"]["MiddleName"]
                    except:
                        pass

                if xsi_type == "Publisher.CentralBankRf.v2":
                    try:
                        publisher_centralbankrf_v2.name = msg_data["Publisher"]["Name"]
                    except:
                        pass
                    try:
                        publisher_centralbankrf_v2.ogrn = msg_data["Publisher"]["Ogrn"]
                    except:
                        pass
                    try:
                        publisher_centralbankrf_v2.inn = msg_data["Publisher"]["Inn"]
                    except:
                        pass

                if xsi_type == "Publisher.Asv.v2":
                    try:
                        publisher_asv_v2.name = msg_data["Publisher"]["Name"]
                    except:
                        pass
                    try:
                        publisher_asv_v2.ogrn = msg_data["Publisher"]["Ogrn"]
                    except:
                        pass
                    try:
                        publisher_asv_v2.inn = msg_data["Publisher"]["Inn"]
                    except:
                        pass

                if xsi_type == "Publisher.FnsDepartment.v2":
                    try:
                        publisher_fnsdepartment_v2.name = msg_data["Publisher"]["Name"]
                    except:
                        pass
                    try:
                        publisher_fnsdepartment_v2.ogrn = msg_data["Publisher"]["Ogrn"]
                    except:
                        pass
                    try:
                        publisher_fnsdepartment_v2.inn = msg_data["Publisher"]["Inn"]
                    except:
                        pass

                if xsi_type == "Publisher.Efrsb.v2":
                    try:
                        publisher_efrsb_v2.name = msg_data["Publisher"]["Name"]
                    except:
                        pass

                if xsi_type == "Publisher.Mfc.v2":
                    try:
                        publisher_mfc_v2.name = msg_data["Publisher"]["Name"]
                    except:
                        pass
                    try:
                        publisher_mfc_v2.ogrn = msg_data["Publisher"]["Ogrn"]
                    except:
                        pass
                    try:
                        publisher_mfc_v2.inn = msg_data["Publisher"]["Inn"]
                    except:
                        pass


                message_info.message_type = msg_data["MessageInfo"]["@MessageType"]
    #
                if message_info.message_type == "ArbitralDecree":
                    try:
                        court_decision.text = msg_data["MessageInfo"]["CourtDecision"]["Text"]
                    except:
                        pass

                    try:
                        court_decision.losses_from_arbitr_manager_actions_ammount = \
                            msg_data["MessageInfo"]["CourtDecision"][
                                "LossesFromArbitrManagerActionsAmount"]
                    except:
                        pass
                    else:
                        court_decision.losses_from_arbitr_manager_actions_ammount = \
                            msg_data["MessageInfo"]["CourtDecision"][
                                "LossesFromArbitrManagerActionsAmount"]["@xsi:nil"]

                    try:
                        court_decision.citizen_not_released_from_responsibility = \
                            msg_data["MessageInfo"]["CourtDecision"][
                                "CitizenNotReleasedFromResponsibility"]
                    except:
                        pass
                    else:
                        court_decision.citizen_not_released_from_responsibility = \
                            msg_data["MessageInfo"]["CourtDecision"][
                                "CitizenNotReleasedFromResponsibility"]["@xsi:nil"]

                    try:
                        court_decision.arbitr_manager_illegal_action_type = msg_data["MessageInfo"]["CourtDecision"][
                            "ArbitrManagerIllegalActionType"]
                    except:
                        pass

                    try:
                        court_decision.decision_made_due_tor_cancellation_restructuring_plan = msg_data["MessageInfo"][
                            "CourtDecision"]["DecisionMadeDueTorCancellationRestructuringPlan"]
                    except:
                        pass
                    else:
                        court_decision.decision_made_due_tor_cancellation_restructuring_plan = msg_data["MessageInfo"][
                            "CourtDecision"]["DecisionMadeDueTorCancellationRestructuringPlan"]["@xsi:nil"]

                    try:
                        court_decision.reason_for_cancellation_restructuring_plan = \
                            msg_data["MessageInfo"]["CourtDecision"][
                                "ReasonForCancellationRestructuringPlan"]
                    except:
                        pass

                    try:
                        court_decision.creditor_claim_register_close_date = msg_data["MessageInfo"]["CourtDecision"][
                            "CreditorClaimRegisterCloseDate"]
                    except:
                        pass
                    else:
                        court_decision.creditor_claim_register_close_date = msg_data["MessageInfo"]["CourtDecision"][
                            "CreditorClaimRegisterCloseDate"]["@xsi:nil"]
                    try:
                        court_decision.creditor_claim_setting_requirements_expiration_date = msg_data["MessageInfo"][
                            "CourtDecision"]["CreditorClaimSettingRequirementsExpirationDate"]
                    except:
                        pass
                    else:
                        court_decision.creditor_claim_setting_requirements_expiration_date = msg_data["MessageInfo"][
                            "CourtDecision"]["CreditorClaimSettingRequirementsExpirationDate"]["@xsi:nil"]
                    try:
                        court_decision.arbitr_manager_type = msg_data["MessageInfo"]["ArbitrManagerType"]
                    except:
                        pass
                    # DecisionType
                    try:
                        decision_type.name = msg_data["MessageInfo"]["CourtDecision"]["DecisionType"]["@Name"]
                    except:
                        pass
                    try:
                        decision_type.Id = msg_data["MessageInfo"]["CourtDecision"]["DecisionType"]["@Id"]
                    except:
                        pass
                    try:
                        # CourtDecree
                        court_decree.court_id = msg_data["MessageInfo"]["CourtDecision"]["CourtDecree"]["CourtId"]
                        court_decree.court_name = msg_data["MessageInfo"]["CourtDecision"]["CourtDecree"]["CourtName"]
                        court_decree.file_number = msg_data["MessageInfo"]["CourtDecision"]["CourtDecree"]["FileNumber"]
                        court_decree.decision_date = msg_data["MessageInfo"]["CourtDecision"]["CourtDecree"]["DecisionDate"]
                    except:
                        pass

                    try:
                        arbitr_manager_info.Id = msg_data["MessageInfo"]["CourtDecision"]["ArbitrManagerInfo"]["Id"]
                        arbitr_manager_info.registry_number = msg_data["MessageInfo"]["CourtDecision"]["ArbitrManagerInfo"][
                            "RegistryNumber"]
                        arbitr_manager_info.first_name = msg_data["MessageInfo"]["CourtDecision"]["ArbitrManagerInfo"][
                            "FirstName"]
                        arbitr_manager_info.middle_name = msg_data["MessageInfo"]["CourtDecision"]["ArbitrManagerInfo"][
                            "MiddleName"]
                        arbitr_manager_info.last_name = msg_data["MessageInfo"]["CourtDecision"]["ArbitrManagerInfo"][
                            "LastName"]
                        arbitr_manager_info.inn = msg_data["MessageInfo"]["CourtDecision"]["ArbitrManagerInfo"]["INN"]
                        arbitr_manager_info.ogrn = msg_data["MessageInfo"]["CourtDecision"]["ArbitrManagerInfo"]["OGRN"]
                        arbitr_manager_info.snils = msg_data["MessageInfo"]["CourtDecision"]["ArbitrManagerInfo"]["SNILS"]
                    except:
                        pass
                    try:
                        legal_case_termination_type.code = \
                            msg_data["MessageInfo"]["CourtDecision"]["LegalCaseTerminationType"]["Code"]

                        legal_case_termination_type.code = \
                            msg_data["MessageInfo"]["CourtDecision"]["LegalCaseTerminationType"][
                                "Description"]
                    except:
                        pass
                    try:
                        procedure_prolongation.date = msg_data["MessageInfo"]["CourtDecision"]["ProcedureProlongation"][
                            "Date"]
                        procedure_prolongation.months = msg_data["MessageInfo"]["CourtDecision"]["ProcedureProlongation"][
                            "Months"]
                        procedure_prolongation.message_number = \
                            msg_data["MessageInfo"]["CourtDecision"]["ProcedureProlongation"]["MessageNumber"]
                    except:
                        pass
                    else:
                        procedure_prolongation.date = msg_data["MessageInfo"]["CourtDecision"]["ProcedureProlongation"][
                            "Date"]["@xsi:nil"]
                        procedure_prolongation.months = msg_data["MessageInfo"]["CourtDecision"]["ProcedureProlongation"][
                            "Months"]["@xsi:nil"]
                        procedure_prolongation.message_number = \
                            msg_data["MessageInfo"]["CourtDecision"]["ProcedureProlongation"]["MessageNumber"]
                    try:
                        cancelled_message.number = msg_data["MessageInfo"]["CourtDecision"]["CancelledMessages"]["Number"]
                    except:
                        pass
                    try:

                        court_decision.next_court_session_date = \
                            msg_data["MessageInfo"]["CourtDecision"]["NextCourtSessionDate"]
                    except:
                        pass

                if message_info.message_type == "Auction":
                    try:
                        auction.is_repeat = json.loads(msg_data["MessageInfo"]["Auction"]["IsRepeat"])
                    except:
                        pass
                    try:
                        auction.date = msg_data["MessageInfo"]["Auction"]["Date"]
                    except:
                        pass
                    try:
                        auction.trade_type = msg_data["MessageInfo"]["Auction"]["TradeType"]
                    except:
                        pass
                    try:
                        auction.price_type = msg_data["MessageInfo"]["Auction"]["PriceType"]
                    except:
                        pass
                    try:
                        auction.text = msg_data["MessageInfo"]["Auction"]["Text"]
                    except:
                        pass
                    try:
                        auction.trade_site = msg_data["MessageInfo"]["Auction"]["TradeSite"]
                    except:
                        pass
                    try:
                        auction.id_trade_place = msg_data["MessageInfo"]["Auction"]["IdTradePlace"]
                    except:
                        pass
                    try:
                        auction.additional_text = msg_data["MessageInfo"]["Auction"]["AdditionalText"]
                    except:
                        pass

                    # Application
                    try:
                        application.time_begin = msg_data["MessageInfo"]["Auction"]["Application"]["TimeBegin"]
                    except:
                        pass
                    try:
                        application.time_end = msg_data["MessageInfo"]["Auction"]["Application"]["TimeEnd"]
                    except:
                        pass
                    try:
                        application.rules = msg_data["MessageInfo"]["Auction"]["Application"]["Rules"]
                    except:
                        pass

                    # LotTable -> AuctionLot
                    try:
                        auction_lot.order = msg_data["MessageInfo"]["Auction"]["LotTable"]["AuctionLot"]["Order"]
                    except:
                        pass
                    try:
                        auction_lot.start_price = msg_data["MessageInfo"]["Auction"]["LotTable"]["AuctionLot"]["StartPrice"]
                    except:
                        pass
                    try:
                        auction_lot.step = msg_data["MessageInfo"]["Auction"]["LotTable"]["AuctionLot"]["Step"]
                    except:
                        pass
                    try:
                        auction_lot.advance = msg_data["MessageInfo"]["Auction"]["LotTable"]["AuctionLot"]["Advance"]
                    except:
                        pass
                    try:
                        auction_lot.description = msg_data["MessageInfo"]["Auction"]["LotTable"]["AuctionLot"]["Description"]
                    except:
                        pass
                    try:
                        auction_lot.auction_step_unit = msg_data["MessageInfo"]["Auction"]["LotTable"]["AuctionLot"][
                            "AuctionStepUnit"]
                    except:
                        pass
                    try:
                        auction_lot.advance_step_unit = msg_data["MessageInfo"]["Auction"]["LotTable"]["AuctionLot"][
                            "AdvanceStepUnit"]
                    except:
                        pass
                    try:
                        auction_lot.price_reduction = \
                        msg_data["MessageInfo"]["Auction"]["LotTable"]["AuctionLot"][
                            "PriceReduction"]
                    except:
                        pass
                        # classifierCollection
                    try:
                        auction_lot_classifier.code = msg_data["MessageInfo"]["Auction"]["LotTable"]["AuctionLot"]["ClassifierCollection"]["AuctionLotClassifier"]["Code"]
                    except:
                        pass
                    try:
                        auction_lot_classifier.name = msg_data["MessageInfo"]["Auction"]["LotTable"]["AuctionLot"]["ClassifierCollection"]["AuctionLotClassifier"]["Name"]
                    except:
                        pass

                if message_info.message_type == "Meeting":
                    try:
                        meeting.text = msg_data["MessageInfo"]["Meeting"]["Text"]
                    except Exception as ex:
                        #print("^"*50)
                        pass
                    try:
                        meeting.meeting_date = msg_data["MessageInfo"]["Meeting"]["MeetingDate"]
                    except:
                        pass
                    # else:
                    #     meeting.meeting_date = msg_data["MessageInfo"]["Meeting"]["MeetingDate"]["@xsi:nil"]
                    try:
                        meeting.meeting_date_begin = msg_data["MessageInfo"]["Meeting"]["MeetingDateBegin"]

                    except:
                        pass
                    # else:
                    #     meeting.meeting_date_begin = msg_data["MessageInfo"]["Meeting"]["MeetingDateBegin"]["@xsi:nil"]
                    try:
                        meeting.meeting_form = msg_data["MessageInfo"]["Meeting"]["MeetingForm"]
                    except:
                        pass
                    try:
                        meeting.registration_date = msg_data["MessageInfo"]["Meeting"]["RegistrationDate"]
                    except:
                        pass
                    # else:
                    #     meeting.registration_date = msg_data["MessageInfo"]["Meeting"]["RegistrationDate"]["@xsi:nil"]
                    try:
                        meeting.registration_time_begin = msg_data["MessageInfo"]["Meeting"]["RegistrationTimeBegin"]
                    except:
                        pass
                    else:
                        meeting.registration_time_begin = msg_data["MessageInfo"]["Meeting"]["RegistrationTimeBegin"][
                            "@xsi:nil"]
                    try:
                        meeting.registration_time_end = msg_data["MessageInfo"]["Meeting"]["RegistrationTimeEnd"]
                    except:
                        pass
                    # else:
                    #     meeting.registration_time_end = msg_data["MessageInfo"]["Meeting"]["RegistrationTimeEnd"][
                    #         "@xsi:nil"]
                    try:
                        meeting.examination_site = msg_data["MessageInfo"]["Meeting"]["ExaminationSite"]
                    except:
                        pass
                    try:
                        meeting.examination_date = msg_data["MessageInfo"]["Meeting"]["ExaminationDate"]
                    except:
                        pass
                    try:
                        meeting.comment = msg_data["MessageInfo"]["Meeting"]["Comment"]
                    except:
                        pass
                    try:
                        meeting.fu_mail_address = msg_data["MessageInfo"]["Meeting"]["FuMailAddress"]
                    except:
                        pass
                    try:
                        meeting.web_address = msg_data["MessageInfo"]["Meeting"]["WebAddress"]
                    except:
                        pass
                    try:
                        meeting.meeting_form = msg_data["MessageInfo"]["Meeting"]["MeetingForm"]
                    except:
                        pass

                if message_info.message_type == "MeetingResult":
                    try:
                        meeting_result.text = msg_data["MessageInfo"]["MeetingResult"]["Text"]
                    except:
                        pass
                    try:
                        meeting_result.meeting_form = msg_data["MessageInfo"]["MeetingResult"]["MeetingForm"]
                    except:
                        pass

                if message_info.message_type == "TradeResult":
                    try:
                        trade_result.text = msg_data["MessageInfo"]["TradeResult"]["Text"]
                    except:
                        pass
                    try:
                        trade_result.id_auction_message = msg_data["MessageInfo"]["TradeResult"]["IdAuctionMessage"]
                    except:
                        pass
                        # trade_result.lot_table = msg_data["MessageInfo"]["TradeResult"]["LotTable"]
                        # TradeResultLot
                    try:
                        trade_result_lot.order = msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Order"]
                    except:
                        pass
                    try:
                        trade_result_lot.description = msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"][
                            "Description"]
                    except:
                        pass
                    try:
                        trade_result_lot.lot_status = msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"][
                            "LotStatus"]
                    except:
                        pass
                    try:
                        trade_result_lot.basis = msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Basis"]
                    except:
                        pass
                    try:

                        auction_lot_classifier.code = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["ClassifierCollection"][
                                "AuctionLotClassifier"]["Code"]
                    except:
                        pass
                    try:
                        auction_lot_classifier.name = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["ClassifierCollection"][
                                "AuctionLotClassifier"]["Name"]
                    except:
                        pass

                    try:
                        check = msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Winner"]
                        check = 'winner'

                        status = check
                    except:
                        pass
                    try:
                        check =  msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Buyer"]
                        check = 'buyer'

                        status = check
                    except:
                        pass
                    # winner
                    try:
                        participant_company.price_offer = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Winner"][
                                "ParticipantCompany"]["PriceOffer"]
                    except:
                        pass
                    try:
                        participant_company.address = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Winner"][
                                "ParticipantCompany"]["Address"]
                    except:
                        pass
                    try:
                        participant_company.inn = \
                        msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Winner"][
                            "ParticipantCompany"][
                            "INN"]
                    except:
                        pass
                    try:
                        participant_company.name = \
                        msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Winner"][
                            "ParticipantCompany"][
                            "Name"]
                    except:
                        pass
                    try:
                        participant_company.ogrn = \
                        msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Winner"][
                            "ParticipantCompany"][
                            "OGRN"]
                    except:
                        pass
                    # winner person
                    try:
                        participant_person.price_offer = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Winner"][
                                "ParticipantPerson"]["PriceOffer"]
                    except:
                        pass
                    try:
                        participant_person.address = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Winner"][
                                "ParticipantPerson"]["Address"]
                    except:
                        pass
                    try:
                        participant_person.inn = \
                        msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Winner"]["ParticipantPerson"][
                            "INN"]
                    except:
                        pass
                    try:
                        participant_person.first_name = \
                        msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Winner"]["ParticipantPerson"][
                            "FirstName"]
                    except:
                        pass
                    try:
                        participant_person.middle_name = \
                        msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Winner"]["ParticipantPerson"][
                            "MiddleName"]
                    except:
                        pass
                    try:
                        participant_person.last_name = \
                        msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Winner"]["ParticipantPerson"][
                            "LastName"]
                    except:
                        pass
                    try:
                        participant_person.ogrnip = \
                        msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Winner"]["ParticipantPerson"][
                            "OGRNIP"]
                    except:
                        pass
                    # Buyer

                    try:
                        participant_company.price_offer = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Buyer"][
                                "ParticipantCompany"]["PriceOffer"]
                    except:
                        pass
                    try:
                        participant_company.address = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Buyer"][
                                "ParticipantCompany"]["Address"]
                    except:
                        pass
                    try:
                        participant_company.inn = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Buyer"][
                                "ParticipantCompany"][
                                "INN"]
                    except:
                        pass
                    try:
                        participant_company.name = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Buyer"][
                                "ParticipantCompany"][
                                "Name"]
                    except:
                        pass
                    try:
                        participant_company.ogrn = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Buyer"][
                                "ParticipantCompany"][
                                "OGRN"]
                    except:
                        pass
                    # winner person
                    try:
                        participant_person.price_offer = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Buyer"][
                                "ParticipantPerson"]["PriceOffer"]
                    except:
                        pass
                    try:
                        participant_person.address = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Buyer"][
                                "ParticipantPerson"]["Address"]
                    except:
                        pass
                    try:
                        participant_person.inn = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Buyer"][
                                "ParticipantPerson"][
                                "INN"]
                    except:
                        pass
                    try:
                        participant_person.first_name = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Buyer"][
                                "ParticipantPerson"][
                                "FirstName"]
                    except:
                        pass
                    try:
                        participant_person.middle_name = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Buyer"][
                                "ParticipantPerson"][
                                "MiddleName"]
                    except:
                        pass
                    try:
                        participant_person.last_name = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Buyer"][
                                "ParticipantPerson"][
                                "LastName"]
                    except:
                        pass
                    try:
                        participant_person.ogrnip = \
                            msg_data["MessageInfo"]["TradeResult"]["LotTable"]["TradeResultLot"]["Buyer"][
                                "ParticipantPerson"][
                                "OGRNIP"]
                    except:
                        pass
    #
                if message_info.message_type == "Other":
                    try:
                        other.text = msg_data["MessageInfo"]["Other"]["Text"]
                    except:
                        pass
    #
                if message_info.message_type == "AppointAdministration":
                    try:
                        appoint_administration.text = msg_data["MessageInfo"]["AppointAdministration"]["Text"]
                    except:
                        pass
                    try:
                        appoint_administration.decision_name = msg_data["MessageInfo"]["AppointAdministration"][
                            "DecisionName"]
                    except:
                        pass
                    try:
                        appoint_administration.decision_date = msg_data["MessageInfo"]["AppointAdministration"][
                            "DecisionDate"]
                    except:
                        pass
                    try:
                        appoint_administration.decision_number = msg_data["MessageInfo"]["AppointAdministration"][
                            "DecisionNumber"]
                    except:
                        pass
                    try:
                        appoint_administration.administration_date_from = msg_data["MessageInfo"]["AppointAdministration"][
                            "AdministrationDateFrom"]
                    except:
                        pass
                    try:
                        appoint_administration.reasons = msg_data["MessageInfo"]["AppointAdministration"]["Reasons"]
                    except:
                        pass
                    try:
                        appoint_administration.members = msg_data["MessageInfo"]["AppointAdministration"]["Members"]
                    except:
                        pass
                    try:
                        appoint_administration.administration_period = msg_data["MessageInfo"]["AppointAdministration"][
                            "AdministrationPeriod"]
                    except:
                        pass
                    # Director
                    try:
                        director.name = msg_data["MessageInfo"]["AppointAdministration"][
                            "Director"]["Name"]
                    except:
                        pass
                    try:
                        director.address = msg_data["MessageInfo"]["AppointAdministration"][
                            "Director"]["Address"]
                    except:
                        pass
                    try:
                        director.id_arbitr_manager = msg_data["MessageInfo"]["AppointAdministration"][
                            "Director"]["IdArbitrManager"]
                    except:
                        pass
                    else:
                        director.id_arbitr_manager = msg_data["MessageInfo"]["AppointAdministration"][
                            "Director"]["IdArbitrManager"]["@xsi:nil"]

                    try:
                        director.inn = msg_data["MessageInfo"]["AppointAdministration"][
                            "Director"]["INN"]
                    except:
                        pass
                    try:
                        director.snils = msg_data["MessageInfo"]["AppointAdministration"][
                            "Director"]["SNILS"]
                    except:
                        pass
                    # sro
                    try:
                        sro.sro_id = msg_data["MessageInfo"]["AppointAdministration"][
                            "Director"]["SRO"]["SroId"]
                    except:
                        pass
                    try:
                        sro.sro_name = msg_data["MessageInfo"]["AppointAdministration"][
                            "Director"]["SRO"]["SroName"]
                    except:
                        pass
                    try:
                        sro.sro_registry_number = msg_data["MessageInfo"]["AppointAdministration"][
                            "Director"]["SRO"]["SroRegistryNumber"]
                    except:
                        pass
                    try:
                        sro.ogrn = msg_data["MessageInfo"]["AppointAdministration"][
                            "Director"]["SRO"]["OGRN"]
                    except:
                        pass
                    try:
                        sro.legal_address = msg_data["MessageInfo"]["AppointAdministration"][
                            "Director"]["SRO"]["LegalAddress"]
                    except:
                        pass
                    try:
                        sro.inn = msg_data["MessageInfo"]["AppointAdministration"][
                            "Director"]["SRO"]["INN"]
                    except:
                        pass
                #print("*"*50)

                if message_info.message_type == "ChangeAdministration":
                    try:
                        change_administration.text = msg_data["MessageInfo"]["ChangeAdministration"]["Text"]
                    except:
                        pass
                    try:
                        change_administration.decision_name = msg_data["MessageInfo"]["ChangeAdministration"]["DecisionName"]
                    except:
                        pass
                    try:
                        change_administration.decision_date = msg_data["MessageInfo"]["ChangeAdministration"]["DecisionDate"]
                    except:
                        pass
                    try:
                        change_administration.decision_number = msg_data["MessageInfo"]["ChangeAdministration"][
                            "DecisionNumber"]
                    except:
                        pass
                    try:
                        change_administration.reasons = msg_data["MessageInfo"]["ChangeAdministration"]["Reasons"]
                    except:
                        pass

                    # Director
                    try:
                        director.name = msg_data["MessageInfo"]["ChangeAdministration"][
                            "Director"]["Name"]
                    except:
                        pass
                    try:
                        director.address = msg_data["MessageInfo"]["ChangeAdministration"][
                            "Director"]["Address"]
                    except:
                        pass
                    try:
                        director.id_arbitr_manager = msg_data["MessageInfo"]["ChangeAdministration"][
                            "Director"]["IdArbitrManager"]
                    except:
                        pass
                    else:
                        director.id_arbitr_manager = msg_data["MessageInfo"]["ChangeAdministration"][
                            "Director"]["IdArbitrManager"]["@xsi:nil"]

                    try:
                        director.inn = msg_data["MessageInfo"]["ChangeAdministration"][
                            "Director"]["INN"]
                    except:
                        pass
                    try:
                        director.snils = msg_data["MessageInfo"]["ChangeAdministration"][
                            "Director"]["SNILS"]
                    except:
                        pass
                    # sro
                    try:
                        sro.sro_id = msg_data["MessageInfo"]["ChangeAdministration"][
                            "Director"]["SRO"]["SroId"]
                    except:
                        pass
                    try:
                        sro.sro_name = msg_data["MessageInfo"]["ChangeAdministration"][
                            "Director"]["SRO"]["SroName"]
                    except:
                        pass
                    try:
                        sro.sro_registry_number = msg_data["MessageInfo"]["ChangeAdministration"][
                            "Director"]["SRO"]["SroRegistryNumber"]
                    except:
                        pass
                    try:
                        sro.ogrn = msg_data["MessageInfo"]["ChangeAdministration"][
                            "Director"]["SRO"]["OGRN"]
                    except:
                        pass
                    try:
                        sro.legal_address = msg_data["MessageInfo"]["ChangeAdministration"][
                            "Director"]["SRO"]["LegalAddress"]
                    except:
                        pass
                    try:
                        sro.inn = msg_data["MessageInfo"]["ChangeAdministration"][
                            "Director"]["SRO"]["INN"]
                    except:
                        pass

                #
                #print("_"*50)
                #print(message_info.message_type)
                if message_info.message_type == "TerminationAdministration":
                    try:
                        termination_administration.text = msg_data["MessageInfo"]["TerminationAdministration"]["Text"]
                    except:
                        pass
                    try:
                        termination_administration.decision_name = msg_data["MessageInfo"]["TerminationAdministration"][
                            "DecisionName"]
                    except:
                        pass
                    try:
                        termination_administration.decision_date = msg_data["MessageInfo"]["TerminationAdministration"][
                            "DecisionDate"]
                    except:
                        pass
                    try:
                        termination_administration.decision_number = msg_data["MessageInfo"]["TerminationAdministration"][
                            "DecisionNumber"]
                    except:
                        pass
                    try:
                        termination_administration.cause = msg_data["MessageInfo"]["TerminationAdministration"][
                            "Cause"]
                    except:
                        pass
                    try:
                        termination_administration.other_cause_description = \
                        msg_data["MessageInfo"]["TerminationAdministration"][
                            "OtherCauseDescription"]
                    except:
                        pass

                    # Director
                    try:
                        director.name = msg_data["MessageInfo"]["TerminationAdministration"][
                            "Director"]["Name"]
                    except:
                        pass
                    try:
                        director.address = msg_data["MessageInfo"]["TerminationAdministration"][
                            "Director"]["Address"]
                    except:
                        pass
                    try:
                        director.id_arbitr_manager = msg_data["MessageInfo"]["TerminationAdministration"][
                            "Director"]["IdArbitrManager"]
                    except:
                        pass
                    else:
                        director.id_arbitr_manager = msg_data["MessageInfo"]["TerminationAdministration"][
                            "Director"]["IdArbitrManager"]["@xsi:nil"]

                    try:
                        director.inn = msg_data["MessageInfo"]["TerminationAdministration"][
                            "Director"]["INN"]
                    except:
                        pass
                    try:
                        director.snils = msg_data["MessageInfo"]["TerminationAdministration"][
                            "Director"]["SNILS"]
                    except:
                        pass
                    # sro
                    try:
                        sro.sro_id = msg_data["MessageInfo"]["TerminationAdministration"][
                            "Director"]["SRO"]["SroId"]
                    except:
                        pass
                    try:
                        sro.sro_name = msg_data["MessageInfo"]["TerminationAdministration"][
                            "Director"]["SRO"]["SroName"]
                    except:
                        pass
                    try:
                        sro.sro_registry_number = msg_data["MessageInfo"]["TerminationAdministration"][
                            "Director"]["SRO"]["SroRegistryNumber"]
                    except:
                        pass
                    try:
                        sro.ogrn = msg_data["MessageInfo"]["TerminationAdministration"][
                            "Director"]["SRO"]["OGRN"]
                    except:
                        pass
                    try:
                        sro.legal_address = msg_data["MessageInfo"]["TerminationAdministration"][
                            "Director"]["SRO"]["LegalAddress"]
                    except:
                        pass
                    try:
                        sro.inn = msg_data["MessageInfo"]["TerminationAdministration"][
                            "Director"]["SRO"]["INN"]
                    except:
                        pass
                #print("-"*50)
                if message_info.message_type == "BeginExecutoryProcess":
                    try:
                        begin_executory_process.text = msg_data["MessageInfo"]["BeginExecutoryProcess"]["Text"]
                    except:
                        pass
                    try:
                        begin_executory_process.date_begin_executory_process = msg_data["MessageInfo"]["BeginExecutoryProcess"][
                            "DateBeginExecutoryProcess"]
                    except:
                        pass
                    try:
                        begin_executory_process.number_executory_process = msg_data["MessageInfo"]["BeginExecutoryProcess"][
                            "NumberExecutoryProcess"]
                    except:
                        pass
                ##printed
                if message_info.message_type == "TransferAssertsForImplementation":
                    try:
                        transfer_assert_for_implementation.text = msg_data["MessageInfo"]["TransferAssertsForImplementation"][
                            "Text"]
                    except:
                        pass
                    try:
                        transfer_assert_for_implementation.date_sumbmit = \
                        msg_data["MessageInfo"]["TransferAssertsForImplementation"]["DateSubmit"]
                    except:
                        pass
                    try:
                        transfer_assert_for_implementation.number_executory_process = \
                        msg_data["MessageInfo"]["TransferAssertsForImplementation"]["NumberExecutoryProcess"]
                    except:
                        pass
                    try:
                        transfer_assert_for_implementation.id_begin_exe_process_message = \
                        msg_data["MessageInfo"]["TransferAssertsForImplementation"]["IdBeginExeProcessMessage"]
                    except:
                        pass

                if message_info.message_type == "Annul":
                    try:
                        annul.text = msg_data["MessageInfo"]["Annul"]["Text"]
                    except:
                        pass
                    try:
                        annul.id_addulmnent_message = msg_data["MessageInfo"]["Annul"]["IdAnnuledMessage"]
                    except:
                        pass
                    try:
                        annul.lock_annuled_message_reason = msg_data["MessageInfo"]["Annul"]["LockAnnuledMessageReason"]
                    except:
                        pass

                if message_info.message_type == "PropertyInventoryResult":
                    try:
                        property_inventory_result.text = msg_data["MessageInfo"]["PropertyInventoryResult"]["Text"]
                    except:
                        pass

                if message_info.message_type == "PropertyEvaluationReport":
                    try:
                        property_evaluation_report.text = msg_data["MessageInfo"]["PropertyEvaluationReport"]["Text"]
                    except:
                        pass
                ##printed
                if message_info.message_type == "SaleContractResult":
                    try:
                        sale_contract_result.text = msg_data["MessageInfo"]["SaleContractResult"]["Text"]
                    except:
                        pass
                    try:
                        sale_contract_result.sale_contract_result_type = msg_data["MessageInfo"]["SaleContractResult"][
                            "SaleContractResultType"]
                    except:
                        pass
                    try:
                        sale_contract_result.date_contract = msg_data["MessageInfo"]["SaleContractResult"]["DateContract"]
                    except:
                        pass
                    try:
                        sale_contract_result.price = msg_data["MessageInfo"]["SaleContractResult"]["Price"]
                    except:
                        pass

                    # FailureWinnerInfo
                    try:
                        failure_winner_info.name = msg_data["MessageInfo"]["SaleContractResult"]["FailureWinnerInfo"][
                            "Name"]
                    except:
                        pass
                    try:
                        failure_winner_info.ogrn = msg_data["MessageInfo"]["SaleContractResult"]["FailureWinnerInfo"][
                            "Ogrn"]
                    except:
                        pass
                    try:
                        failure_winner_info.inn = msg_data["MessageInfo"]["SaleContractResult"]["FailureWinnerInfo"]["Inn"]
                    except:
                        pass
                    # PurchaserInfo
                    # FailureWinnerInfo
                    try:
                        purchaser_info.name = msg_data["MessageInfo"]["SaleContractResult"]["FailureWinnerInfo"][
                            "Name"]
                    except:
                        pass
                    try:
                        purchaser_info.ogrn = msg_data["MessageInfo"]["SaleContractResult"]["FailureWinnerInfo"][
                            "Ogrn"]
                    except:
                        pass
                    try:
                        purchaser_info.inn = msg_data["MessageInfo"]["SaleContractResult"]["FailureWinnerInfo"][
                            "Inn"]
                    except:
                        pass
                #print("\\" * 50)
                try:
                    if message_info.message_type == "SaleContractResult2":
                        try:
                            sale_contract_result2.text = msg_data["MessageInfo"]["SaleContractResult2"]["Text"]
                        except:
                            pass
                        try:
                            sale_contract_result2.id_auction_message = msg_data["MessageInfo"]["SaleContractResult2"][
                                "IdAuctionMessage"]
                        except:
                            pass
                        else:
                            sale_contract_result2.id_auction_message = msg_data["MessageInfo"]["SaleContractResult2"][
                                "IdAuctionMessage"]["@xsi:nil"]
                        try:
                            sale_contract_result2.trade_place_name = msg_data["MessageInfo"]["SaleContractResult2"][
                                "TradePlaceName"]
                        except:
                            pass
                        try:
                            sale_contract_result2.trade_number = msg_data["MessageInfo"]["SaleContractResult2"]["TradeNumber"]
                        except:
                            pass

                            # contracts saleContracInfo
                        try:

                            sale_contract_info.type_sale_contract_info = \
                            msg_data["MessageInfo"]["SaleContractResult2"]["Contracts"]["SaleContractInfo"]["@xsi:type"]
                        except:
                            pass
                        try:
                            sale_contract_info.lot_number = \
                            msg_data["MessageInfo"]["SaleContractResult2"]["Contracts"]["SaleContractInfo"]["LotNumber"]
                        except:
                            pass
                        try:
                            sale_contract_info.description = \
                            msg_data["MessageInfo"]["SaleContractResult2"]["Contracts"]["SaleContractInfo"]["Description"]
                        except:
                            pass
                        try:
                            sale_contract_info.conclusion_info = \
                                msg_data["MessageInfo"]["SaleContractResult2"]["Contracts"]["SaleContractInfo"]["ConclusionInfo"]
                        except:
                            pass
                        try:
                            sale_contract_info.number = \
                                msg_data["MessageInfo"]["SaleContractResult2"]["Contracts"]["SaleContractInfo"]["Number"]
                        except:
                            pass
                        try:
                            sale_contract_info.conclusion_date = \
                                msg_data["MessageInfo"]["SaleContractResult2"]["Contracts"]["SaleContractInfo"]["ConclusionDate"]
                        except:
                            pass
                        try:
                            sale_contract_info.property_purchase_price = \
                                msg_data["MessageInfo"]["SaleContractResult2"]["Contracts"]["SaleContractInfo"][
                                    "PropertyPurchasePrice"]
                        except:
                            pass
                        try:
                            failure_winner_info.name = \
                            msg_data["MessageInfo"]["SaleContractResult2"]["Contracts"]["SaleContractInfo"][
                                "FailureWinnerInfo"]["Name"]
                        except:
                            pass
                        try:
                            failure_winner_info.ogrn = \
                            msg_data["MessageInfo"]["SaleContractResult2"]["Contracts"]["SaleContractInfo"][
                                "FailureWinnerInfo"]["Ogrn"]
                        except:
                            pass
                        try:
                            failure_winner_info.inn = \
                            msg_data["MessageInfo"]["SaleContractResult2"]["Contracts"]["SaleContractInfo"][
                                "FailureWinnerInfo"]["Inn"]
                        except:
                            pass


                        # PurchaserInfo
                        # FailureWinnerInfo
                        try:
                            purchaser_info.name = \
                            msg_data["MessageInfo"]["SaleContractResult2"]["Contracts"]["SaleContractInfo"]["PurchaserInfo"][
                                "Name"]
                        except:
                            pass
                        try:
                            purchaser_info.ogrn = msg_data["MessageInfo"]["SaleContractResult"]["PurchaserInfo"][
                                "Ogrn"]
                        except:
                            pass
                        try:
                            purchaser_info.inn = msg_data["MessageInfo"]["SaleContractResult"]["PurchaserInfo"][
                                "Inn"]
                        except:
                            pass
                except Exception as ex:
                    pass

                if message_info.message_type == "Committee":
                    try:
                        committee.text = msg_data["MessageInfo"]["Committee"]["Text"]
                    except:
                        pass
                    try:
                        committee.meeting_site = msg_data["MessageInfo"]["Committee"]["MeetingSite"]
                    except:
                        pass
                    try:
                        committee.meeting_date = msg_data["MessageInfo"]["Committee"]["MeetingDate"]
                    except:
                        pass

                if message_info.message_type == "CommitteeResult":
                    try:
                        other.text = msg_data["MessageInfo"]["Other"]["Text"]
                    except:
                        pass
                #not #printed
                if message_info.message_type == "SaleOrderPledgedProperty":
                    try:
                        sale_order_pledged_property.text = msg_data["MessageInfo"]["SaleOrderPledgedProperty"]["Text"]
                    except:
                        pass
                    try:
                        sale_order_pledged_property.meeting_date = msg_data["MessageInfo"]["SaleOrderPledgedProperty"]["MeetingDate"]
                    except:
                        pass
                    try:
                        sale_order_pledged_property.trade_site = msg_data["MessageInfo"]["SaleOrderPledgedProperty"]["TradeSite"]
                    except:
                        pass
                    try:
                        sale_order_pledged_property.id_trade_place = msg_data["MessageInfo"]["SaleOrderPledgedProperty"]["IdTradePlace"]
                    except:
                        pass
                    try:
                        sale_order_pledged_property.additional_text = msg_data["MessageInfo"]["SaleOrderPledgedProperty"]["AdditionalText"]
                    except:
                        pass

                    #LotTable PledgedPropertyLot уточнить
                    # sale_order_pledged_property.additional_text = msg_data["MessageInfo"]["SaleOrderPledgedProperty"]["AdditionalText"]
                try:
                    if message_info.message_type == "ReceivingCreditorDemand":
                        try:
                            receiving_creditor_demand.text = msg_data["MessageInfo"]["ReceivingCreditorDemand"]["Text"]
                        except:
                            pass
                        try:
                            receiving_creditor_demand.demand_date = msg_data["MessageInfo"]["ReceivingCreditorDemand"]["DemandDate"]
                        except:
                            pass
                        try:
                            receiving_creditor_demand.demand_sum = msg_data["MessageInfo"]["ReceivingCreditorDemand"]["DemandSum"]
                        except:
                            pass
                        try:
                            receiving_creditor_demand.creditor_name = msg_data["MessageInfo"]["ReceivingCreditorDemand"]["CreditorName"]
                        except:
                            pass
                        try:
                            receiving_creditor_demand.reason_occurance = msg_data["MessageInfo"]["ReceivingCreditorDemand"]["ReasonOccurence"]
                        except:
                            pass
                except Exception as ex:
                    pass
                if message_info.message_type == "DemandAnnouncement":
                    try:
                        other.text = msg_data["MessageInfo"]["Other"]["Text"]
                    except:
                        pass
                if message_info.message_type == "CourtAssertAcceptance":
                    try:
                        other.text = msg_data["MessageInfo"]["Other"]["Text"]
                    except:
                        pass
                if message_info.message_type == "FinancialStateInformation":
                    try:
                        other.text = msg_data["MessageInfo"]["Other"]["Text"]
                    except:
                        pass
                if message_info.message_type == "BankPayment":
                    try:
                        other.text = msg_data["MessageInfo"]["Other"]["Text"]
                    except:
                        pass
                if message_info.message_type == "AssetsReturning":
                    try:
                        other.text = msg_data["MessageInfo"]["Other"]["Text"]
                    except:
                        pass
                if message_info.message_type == "CourtAcceptanceStatement":
                    try:
                        other.text = msg_data["MessageInfo"]["Other"]["Text"]
                    except:
                        pass

                if message_info.message_type == "DeliberateBankruptcy":
                    try:
                        deliberate_bankruptcy.text = msg_data["MessageInfo"]["DeliberateBankruptcy"]["Text"]
                    except:
                        pass
                    try:
                        deliberate_bankruptcy.deliberate_bankruptcy_signs = msg_data["MessageInfo"]["DeliberateBankruptcy"]["DeliberateBankruptcySigns"]
                    except:
                        pass
                    try:
                        deliberate_bankruptcy.deliberate_signs_not_searched_reason = msg_data["MessageInfo"]["DeliberateBankruptcy"]["DeliberateSignsNotSearchedReason"]
                    except:
                        pass
                    try:
                        deliberate_bankruptcy.fake_bankruptcy_signs = msg_data["MessageInfo"]["DeliberateBankruptcy"]["FakeBankruptcySigns"]
                    except:
                        pass
                    try:
                        deliberate_bankruptcy.fake_signs_not_searched_reason = msg_data["MessageInfo"]["DeliberateBankruptcy"]["FakeSignsNotSearchedReason"]
                    except:
                        pass
                if message_info.message_type == "ChangeDeliberateBankruptcy":
                    try:
                        change_deliberate_bankruptcy.text = msg_data["MessageInfo"]["ChangeDeliberateBankruptcy"]["Text"]
                    except:
                        pass
                    try:
                        change_deliberate_bankruptcy.deliberate_bankruptcy_signs = msg_data["MessageInfo"]["ChangeDeliberateBankruptcy"]["DeliberateBankruptcySigns"]
                    except:
                        pass
                    try:
                        change_deliberate_bankruptcy.deliberate_signs_not_searched_reason = msg_data["MessageInfo"]["ChangeDeliberateBankruptcy"]["DeliberateSignsNotSearchedReason"]
                    except:
                        pass
                    try:
                        change_deliberate_bankruptcy.fake_bankruptcy_signs = msg_data["MessageInfo"]["ChangeDeliberateBankruptcy"]["FakeBankruptcySigns"]
                    except:
                        pass
                    try:
                        change_deliberate_bankruptcy.fake_signs_not_searched_reason = msg_data["MessageInfo"]["ChangeDeliberateBankruptcy"]["FakeSignsNotSearchedReason"]
                    except:
                        pass
                    try:
                        change_deliberate_bankruptcy.id_cancelled_message = \
                        msg_data["MessageInfo"]["ChangeDeliberateBankruptcy"]["IdCanceledMessage"]
                    except:
                        pass
                if message_info.message_type == "IntentionCreditOrg":
                    try:
                        intention_credit_org.text = msg_data["MessageInfo"]["IntentionCreditOrg"]["Text"]
                    except:
                        pass
                if message_info.message_type == "LiabilitiesCreditOrg":
                    try:
                        liabilities_credit_org.text = msg_data["MessageInfo"]["LiabilitiesCreditOrg"]["Text"]
                    except:
                        pass
                if message_info.message_type == "PerformanceCreditOrg":
                    try:
                        perfomance_credit_org.text = msg_data["MessageInfo"]["PerformanceCreditOrg"]["Text"]
                    except:
                        pass
                if message_info.message_type == "BuyingProperty":
                    try:
                        buying_property.text = msg_data["MessageInfo"]["BuyingProperty"]["Text"]
                    except:
                        pass

                if message_info.message_type == "DeclarationPersonDamages":
                    try:
                        declaration_person_damages.text = msg_data["MessageInfo"]["DeclarationPersonDamages"]["Text"]
                    except:
                        pass

                    #BankruptSuprvisoryPersons - > BankruptSupervisoryPerson
                    try:
                        bankrupt_supervisory_person.bankrupt_supervisory_person = msg_data["MessageInfo"]["DeclarationPersonDamages"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["@xsi:type"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.responsibility_amount = msg_data["MessageInfo"]["DeclarationPersonDamages"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["ResponsibilityAmount"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.name = msg_data["MessageInfo"]["DeclarationPersonDamages"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Name"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code = msg_data["MessageInfo"]["DeclarationPersonDamages"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Code"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code_type = \
                        msg_data["MessageInfo"]["DeclarationPersonDamages"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["CodeType"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.country = \
                        msg_data["MessageInfo"]["DeclarationPersonDamages"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["CodeType"]
                    except:
                        pass
                    #AnotherPersonForResponsibility -  > PersonForResponsibility
                    try:
                        person_for_responsibility.fio = \
                        msg_data["MessageInfo"]["DeclarationPersonDamages"][
                            "AnotherPersonsForResponsibility"]["Fio"]
                    except:
                        pass
                    try:
                        person_for_responsibility.type_person_responsibility = \
                        msg_data["MessageInfo"]["DeclarationPersonDamages"][
                            "AnotherPersonsForResponsibility"]["Type"]
                    except:
                        pass
                    try:
                        person_for_responsibility.responsibility_amount = \
                        msg_data["MessageInfo"]["DeclarationPersonDamages"][
                            "AnotherPersonsForResponsibility"]["ResponsibilityAmount"]
                    except:
                        pass

                if message_info.message_type == "ActPersonDamages":
                    try:
                        act_person_damages.text = msg_data["MessageInfo"]["ActPersonDamages"]["Text"]
                    except:
                        pass
                    try:
                        act_person_damages.declaration_person_damages_message_id = msg_data["MessageInfo"][
                            "ActPersonDamages"]["DeclarationPersonDamagesMessageId"]
                    except:
                        pass

                    try:
                        bankrupt_supervisory_person.bankrupt_supervisory_person = msg_data["MessageInfo"][
                            "ActPersonDamages"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["@xsi:type"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.responsibility_amount = msg_data["MessageInfo"][
                            "ActPersonDamages"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["ResponsibilityAmount"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.name = msg_data["MessageInfo"]["ActPersonDamages"][
                            "BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Name"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code = msg_data["MessageInfo"]["ActPersonDamages"][
                            "BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Code"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code_type = \
                        msg_data["MessageInfo"]["ActPersonDamages"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["CodeType"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.country = \
                        msg_data["MessageInfo"]["ActPersonDamages"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["CodeType"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.is_arraignment = \
                        msg_data["MessageInfo"]["ActPersonDamages"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["IsArraignment"]
                    except:
                        pass
                    #AnotherPersonForResponsibility -  > PersonForResponsibility
                    try:
                        person_for_responsibility.fio = \
                        msg_data["MessageInfo"]["ActPersonDamages"][
                            "AnotherPersonsForResponsibility"]["PersonForResponsibility"]["Fio"]
                    except:
                        pass
                    try:
                        person_for_responsibility.type_person_responsibility = \
                        msg_data["MessageInfo"]["ActPersonDamages"][
                            "AnotherPersonsForResponsibility"]["PersonForResponsibility"]["Type"]
                    except:
                        pass
                    try:
                        person_for_responsibility.responsibility_amount = \
                        msg_data["MessageInfo"]["ActPersonDamages"][
                            "AnotherPersonsForResponsibility"]["PersonForResponsibility"]["ResponsibilityAmount"]
                    except:
                        pass
                    try:
                        person_for_responsibility.is_arraignment = \
                        msg_data["MessageInfo"]["ActPersonDamages"][
                            "AnotherPersonsForResponsibility"]["PersonForResponsibility"]["IsArraignment"]
                    except:
                        pass

                if message_info.message_type == "ActReviewPersonDamages":
                    try:
                        act_review_person_damages.text = msg_data["MessageInfo"]["ActReviewPersonDamages"]["Text"]
                    except:
                        pass
                    try:
                        act_review_person_damages.act_person_damages_message_id = msg_data["MessageInfo"]["ActReviewPersonDamages"]["ActPersonDamagesMessageId"]
                    except:
                        pass

                    try:
                        bankrupt_supervisory_person.bankrupt_supervisory_person = msg_data["MessageInfo"][
                            "ActReviewPersonDamages"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["@xsi:type"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.responsibility_amount = msg_data["MessageInfo"][
                            "ActReviewPersonDamages"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["ResponsibilityAmount"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.name = msg_data["MessageInfo"]["ActReviewPersonDamages"][
                            "BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Name"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code = msg_data["MessageInfo"]["ActReviewPersonDamages"][
                            "BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Code"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code_type = \
                        msg_data["MessageInfo"]["ActReviewPersonDamages"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["CodeType"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.country = \
                        msg_data["MessageInfo"]["ActReviewPersonDamages"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["Country"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.is_arraignment = \
                        msg_data["MessageInfo"]["ActReviewPersonDamages"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["IsArraignment"]
                    except:
                        pass
                    #AnotherPersonForResponsibility -  > PersonForResponsibility
                    try:
                        person_for_responsibility.fio = \
                        msg_data["MessageInfo"]["ActReviewPersonDamages"][
                            "AnotherPersonsForResponsibility"]["Fio"]
                    except:
                        pass
                    try:
                        person_for_responsibility.type_person_responsibility = \
                        msg_data["MessageInfo"]["ActReviewPersonDamages"][
                            "AnotherPersonsForResponsibility"]["PersonForResponsibility"]["Type"]
                    except:
                        pass
                    try:
                        person_for_responsibility.responsibility_amount = \
                        msg_data["MessageInfo"]["ActReviewPersonDamages"][
                            "AnotherPersonsForResponsibility"]["PersonForResponsibility"]["ResponsibilityAmount"]
                    except:
                        pass
                    try:
                        person_for_responsibility.is_arraignment = \
                        msg_data["MessageInfo"]["ActReviewPersonDamages"][
                            "AnotherPersonsForResponsibility"]["PersonForResponsibility"]["IsArraignment"]
                    except:
                        pass

                if message_info.message_type == "DealInvalid":
                    try:

                        deal_invalid.text = msg_data["MessageInfo"]["DealInvalid"]["Text"]
                    except:
                        pass
                    try:
                        deal_invalid.is_apply_by_arbitr_manager = json.loads(msg_data["MessageInfo"]["DealInvalid"]["IsApplyByArbitrManager"])
                    except:
                        pass
                    try:
                        deal_invalid.declaration_notice_date = msg_data["MessageInfo"]["DealInvalid"][
                            "DeclarationNoticeDate"]
                    except:
                        pass
                    else:
                        deal_invalid.declaration_notice_date = msg_data["MessageInfo"]["DealInvalid"][
                            "DeclarationNoticeDate"]["@xsi:nil"]
                    try:
                        deal_invalid.declaration_date = msg_data["MessageInfo"]["DealInvalid"][
                            "DeclarationDate"]
                    except:
                        pass
                    try:
                        for i in range(msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"]):
                            deal_participant.deal_participant = msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"][i]["@xsi:type"]
                            deal_participant.name = \
                            msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"][i]["Name"]
                            deal_participant.code = \
                            msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"][i]["Code"]
                            deal_participant.save()
                            deal_participants.deal_participant = deal_participants
                            deal_participants.save()
                    except:
                        pass
                    try:
                        deal_participant.deal_participant = \
                        msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"]["@xsi:type"]
                        deal_participant.name = \
                            msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"]["Name"]
                        deal_participant.code = \
                            msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"]["Code"]
                    except:
                        pass
                if message_info.message_type == "ActDealInvalid":
                    try:
                        act_deal_invalid.text = buying_property.text = msg_data["MessageInfo"]["ActDealInvalid"]["Text"]
                    except:
                        pass
                    try:
                        act_deal_invalid.deal_invalid_message_id = msg_data["MessageInfo"]["ActDealInvalid"]["DealInvalidMessageId"]
                    except:
                        pass
                    try:
                        act_deal_invalid.deal_not_valid = json.loads(msg_data["MessageInfo"]["ActDealInvalid"]["DealNotValid"])
                    except:
                        pass
                    try:

                        act_deal_invalid.court_decision_notice_date = msg_data["MessageInfo"]["ActDealInvalid"]["CourtDecisionNoticeDate"]
                    except:
                        pass


                    try:
                        for i in range(msg_data["MessageInfo"]["ActDealInvalid"]["DealParticipants"]["DealParticipant"]):
                            deal_participant.deal_participant = msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"][i]["@xsi:type"]
                            deal_participant.name = \
                            msg_data["MessageInfo"]["ActDealInvalid"]["DealParticipants"]["DealParticipant"][i]["Name"]
                            deal_participant.code = \
                            msg_data["MessageInfo"]["ActDealInvalid"]["DealParticipants"]["DealParticipant"][i]["Code"]
                            deal_participant.deal_participant = \
                            msg_data["MessageInfo"]["ActDealInvalid"]["DealParticipants"]["DealParticipant"][i]["@xsi:type"]
                            deal_participant.code_type = \
                                msg_data["MessageInfo"]["ActDealInvalid"]["DealParticipants"]["DealParticipant"][i][
                                    "CodeType"]
                            deal_participant.country = \
                                msg_data["MessageInfo"]["ActDealInvalid"]["DealParticipants"]["DealParticipant"][i][
                                    "Country"]
                            deal_participant.save()
                            deal_participants.deal_participant = deal_participants
                            deal_participants.save()
                    except:
                        pass
                    try:
                        deal_participant.deal_participant = \
                        msg_data["MessageInfo"]["ActDealInvalid"]["DealParticipants"]["DealParticipant"]["@xsi:type"]
                        deal_participant.name = \
                            msg_data["MessageInfo"]["ActDealInvalid"]["DealParticipants"]["DealParticipant"]["Name"]
                        deal_participant.code = \
                            msg_data["MessageInfo"]["ActDealInvalid"]["DealParticipants"]["DealParticipant"]["Code"]


                        deal_participant.code_type = \
                            msg_data["MessageInfo"]["ActDealInvalid"]["DealParticipants"]["DealParticipant"][
                                "CodeType"]
                        deal_participant.country = \
                            msg_data["MessageInfo"]["ActDealInvalid"]["DealParticipants"]["DealParticipant"][
                                "Country"]
                    except:
                        pass

                if message_info.message_type == "ActDealInvalid2":
                    try:
                        act_deal_invalid2.text = msg_data["MessageInfo"]["ActDealInvalid2"]["Text"]
                    except:
                        pass
                    try:
                        act_deal_invalid2.court_decision_notice_date = msg_data["MessageInfo"]["ActDealInvalid2"]["CourtDecisionNoticeDate"]
                    except:
                        pass

                        #Deals - > DealInfo
                    try:
                        deal_info.deal_invalid_message_id = msg_data["MessageInfo"]["ActDealInvalid2"]["Deals"]["DealInfo"]["DealInvalidMessageId"]
                    except:
                        pass
                    try:
                        deal_info.deal_invalid_message_date = msg_data["MessageInfo"]["ActDealInvalid2"]["Deals"]["DealInfo"]["DealInvalidMessageDate"]
                    except:
                        pass
                    try:
                        deal_info.deal_invalid_message_number = msg_data["MessageInfo"]["ActDealInvalid2"]["Deals"]["DealInfo"]["DealInvalidMessageNumber"]
                    except:
                        pass
                    try:
                        deal_info.deal_not_valid = json.loads(msg_data["MessageInfo"]["ActDealInvalid2"]["Deals"]["DealInfo"]["DealNotValid"])
                    except:
                        pass
                    try:
                        deal_info.deal_invalid_message_id = msg_data["MessageInfo"]["ActDealInvalid2"]["Deals"]["DealInfo"]["DealInvalidMessageId"]
                    except:
                        pass

                    try:
                        for i in range(msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"]):
                            deal_participant.deal_participant = msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"][i]["@xsi:type"]
                            deal_participant.name = \
                            msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"][i]["Name"]
                            deal_participant.code = \
                            msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"][i]["Code"]
                            deal_participant.deal_participant = \
                            msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"][i]["@xsi:type"]
                            deal_participant.code_type = \
                                msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"][i][
                                    "CodeType"]
                            deal_participant.country = \
                                msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"][i][
                                    "Country"]
                            deal_participant.save()
                            deal_participants.deal_participant = deal_participants
                            deal_participants.save()
                    except:
                        pass
                    try:

                        deal_participant.deal_participant = \
                        msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"]["@xsi:type"]
                        deal_participant.name = \
                            msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"]["Name"]
                        deal_participant.code = \
                            msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"]["Code"]


                        deal_participant.code_type = \
                            msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"][
                                "CodeType"]
                        deal_participant.country = \
                            msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"][
                                "Country"]
                    except:
                        pass

                if message_info.message_type == "ActReviewDealInvalid":
                    try:
                        act_review_deal_invalid.text = msg_data["MessageInfo"]["ActReviewDealInvalid"]["Text"]
                    except:
                        pass
                    try:
                        act_review_deal_invalid.deal_not_valid = json.loads(msg_data["MessageInfo"]["ActReviewDealInvalid"]["Deals"]["DealInfo"]["DealNotValid"])
                    except:
                        pass
                    try:
                        act_review_deal_invalid.deal_invalid_message_id = msg_data["MessageInfo"]["ActReviewDealInvalid"]["Deals"]["DealInfo"]["DealInvalidMessageId"]
                    except:
                        pass
                    try:
                        act_review_deal_invalid.court = msg_data["MessageInfo"]["ActReviewDealInvalid"]["Deals"]["DealInfo"]["DealInvalidMessageId"]
                    except:
                        pass
                    try:
                        for i in range(msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"]):
                            deal_participant.deal_participant = \
                            msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"][i]["@xsi:type"]
                            deal_participant.name = \
                                msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"][i]["Name"]
                            deal_participant.code = \
                                msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"][i]["Code"]
                            deal_participant.deal_participant = \
                                msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"][i][
                                    "@xsi:type"]
                            deal_participant.code_type = \
                                msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"][i][
                                    "CodeType"]
                            deal_participant.country = \
                                msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"][i][
                                    "Country"]
                            deal_participant.save()
                            deal_participants.deal_participant = deal_participants
                            deal_participants.save()
                    except:
                        pass
                    try:
                        deal_participant.deal_participant = \
                            msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"]["@xsi:type"]
                        deal_participant.name = \
                            msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"]["Name"]
                        deal_participant.code = \
                            msg_data["MessageInfo"]["ActDealInvalid2"]["DealParticipants"]["DealParticipant"]["Code"]

                        deal_participant.code_type = \
                            msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"][
                                "CodeType"]
                        deal_participant.country = \
                            msg_data["MessageInfo"]["DealInvalid"]["DealParticipants"]["DealParticipant"][
                                "Country"]
                    except:
                        pass
    #
                if message_info.message_type == "ActReviewDealInvalid2":
                    try:
                        act_review_deal_invalid2.text =  msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Text"]
                    except:
                        pass
                    try:
                        act_review_deal_invalid2.court_decision_notice_date =  msg_data["MessageInfo"]["ActReviewDealInvalid2"]["CourtDecisionNoticeDate"]
                    except:
                        pass
                    try:
                        #Acts -> ActInfo
                        act_info.act_deal_invalid_message_id = msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["ActDealInvalidMessageId"]
                    except:
                        pass
                    try:
                        act_info.act_deal_invalid_message_date = msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["ActDealInvalidMessageDate"]
                    except:
                        pass
                    try:
                        act_info.act_deal_invalid_message_number = msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["ActDealInvalidMessageNumber"]
                    except:
                        pass
                        #Deal -> DealInfo
                    try:
                        deal_info.deal_invalid_message_id = msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"]["DealInfo"]["DealInvalidMessageId"]
                    except:
                        pass
                    try:
                        deal_info.deal_invalid_message_date = msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"]["DealInfo"]["DealInvalidMessageDate"]
                    except:
                        pass
                    try:
                        deal_info.deal_invalid_message_number = msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"]["DealInfo"]["DealInvalidMessageNumber"]
                    except:
                        pass
                    try:
                        deal_info.deal_not_valid = json.loads(msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"]["DealInfo"]["DealNotValid"])
                    except:
                        pass

                     #deal participants -> participant
                    try:
                        for i in range(msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"]["DealInfo"]["DealParticipants"]):
                            deal_participant.deal_participant = msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"]["DealInfo"]["DealParticipants"]["DealParticipant"][i]["@xsi:type"]
                            deal_participant.name = \
                            msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"]["DealInfo"]["DealParticipants"]["DealParticipant"][i]["Name"]
                            deal_participant.code = \
                                msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"][
                                    "DealInfo"]["DealParticipants"]["DealParticipant"][i]["Code"]
                            deal_participant.deal_participant = \
                            msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"]["DealInfo"]["DealParticipants"]["DealParticipant"][i]["@xsi:type"]
                            deal_participant.code_type = \
                                msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"]["DealInfo"]["DealParticipants"]["DealParticipant"][i][
                                    "CodeType"]
                            deal_participant.country = \
                                msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"]["DealInfo"]["DealParticipants"]["DealParticipant"][i][
                                    "Country"]
                            deal_participant.save()
                            deal_participants.deal_participant = deal_participants
                            deal_participants.save()
                    except:
                        pass
                    #dpart
                    try:
                        deal_participant.deal_participant = \
                        msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"]["DealInfo"]["DealParticipants"]["DealParticipant"]["@xsi:type"]
                        deal_participant.name = \
                            msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"]["DealInfo"]["DealParticipants"]["DealParticipant"]["Name"]
                        deal_participant.code = \
                            msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"][
                                "DealInfo"]["DealParticipants"]["DealParticipant"]["Code"]


                        deal_participant.code_type = \
                            msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"][
                                "DealInfo"]["DealParticipants"]["DealParticipant"][
                                "CodeType"]
                        deal_participant.country = \
                            msg_data["MessageInfo"]["ActReviewDealInvalid2"]["Acts"]["ActInfo"]["Deals"][
                                "DealInfo"]["DealParticipants"]["DealParticipant"][
                                "Country"]
                    except:
                        pass

                if message_info.message_type == "DeclarationPersonSubsidiary":
                    try:
                        declaration_person_subsidiary.text = msg_data["MessageInfo"]["DeclarationPersonSubsidiary"]["Text"]
                    except:
                        pass

                    try:
                        bankrupt_supervisory_person.bankrupt_supervisory_person = msg_data["MessageInfo"][
                            "DeclarationPersonSubsidiary"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["@xsi:type"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.responsibility_amount = msg_data["MessageInfo"][
                            "DeclarationPersonSubsidiary"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["ResponsibilityAmount"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.name = msg_data["MessageInfo"]["DeclarationPersonSubsidiary"][
                            "BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Name"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code = msg_data["MessageInfo"]["DeclarationPersonSubsidiary"][
                            "BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Code"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code_type = \
                        msg_data["MessageInfo"]["DeclarationPersonSubsidiary"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["CodeType"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.country = \
                        msg_data["MessageInfo"]["DeclarationPersonSubsidiary"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["Country"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.is_arraignment = \
                        msg_data["MessageInfo"]["DeclarationPersonSubsidiary"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["IsArraignment"]
                    except:
                        pass

                if message_info.message_type == "ActPersonSubsidiary":
                    try:
                        act_person_subsidiary.text = msg_data["MessageInfo"]["ActPersonSubsidiary"]["Text"]
                    except:
                        pass
                    try:
                        act_person_subsidiary.declaration_person_subsidiary_message_id = msg_data["MessageInfo"]["ActPersonSubsidiary"]["DeclarationPersonSubsidiaryMessageId"]
                    except:
                        pass

                    try:
                        bankrupt_supervisory_person.bankrupt_supervisory_person = msg_data["MessageInfo"][
                            "ActPersonSubsidiary"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["@xsi:type"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.responsibility_amount = msg_data["MessageInfo"][
                            "ActPersonSubsidiary"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["ResponsibilityAmount"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.name = msg_data["MessageInfo"]["ActPersonSubsidiary"][
                            "BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Name"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code = msg_data["MessageInfo"]["ActPersonSubsidiary"][
                            "BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Code"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code_type = \
                        msg_data["MessageInfo"]["ActPersonSubsidiary"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["CodeType"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.country = \
                        msg_data["MessageInfo"]["ActPersonSubsidiary"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["Country"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.is_arraignment = \
                        msg_data["MessageInfo"]["ActPersonSubsidiary"]["BankruptSupervisoryPersons"][
                            "BankruptSupervisoryPerson"]["IsArraignment"]
                    except:
                        pass

                if message_info.message_type == "ActReviewPersonSubsidiary":
                    try:
                        act_review_person_subsidiary.text = msg_data["MessageInfo"]["ActReviewPersonSubsidiary"]["Text"]
                    except:
                        pass
                    try:
                        act_review_person_subsidiary.act_person_subsidiary_id= msg_data["MessageInfo"]["ActReviewPersonSubsidiary"]["ActPersonSubsidiaryId"]
                    except:
                        pass

                    try:
                        bankrupt_supervisory_person.bankrupt_supervisory_person = msg_data["MessageInfo"][
                            "ActReviewPersonSubsidiary"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["@xsi:type"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.responsibility_amount = msg_data["MessageInfo"][
                            "ActReviewPersonSubsidiary"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"][
                            "ResponsibilityAmount"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.name = msg_data["MessageInfo"]["ActReviewPersonSubsidiary"][
                            "BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Name"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code = msg_data["MessageInfo"]["ActReviewPersonSubsidiary"][
                            "BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Code"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code_type = \
                            msg_data["MessageInfo"]["ActReviewPersonSubsidiary"]["BankruptSupervisoryPersons"][
                                "BankruptSupervisoryPerson"]["CodeType"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.country = \
                            msg_data["MessageInfo"]["ActReviewPersonSubsidiary"]["BankruptSupervisoryPersons"][
                                "BankruptSupervisoryPerson"]["Country"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.is_arraignment = \
                            msg_data["MessageInfo"]["ActReviewPersonSubsidiary"]["BankruptSupervisoryPersons"][
                                "BankruptSupervisoryPerson"]["IsArraignment"]
                    except:
                        pass

                if message_info.message_type == "MeetingWorker":
                    try:
                        meeting_worker.text = msg_data["MessageInfo"]["MeetingWorker"]["Text"]
                    except:
                        pass
                    try:
                        meeting_worker.meeting_form = msg_data["MessageInfo"]["MeetingWorker"]["MeetingForm"]
                    except:
                        pass
                    try:
                        meeting_worker.meeting_date = msg_data["MessageInfo"]["MeetingWorker"]["MeetingDate"]
                    except:
                        pass
                    else:
                        meeting_worker.meeting_date = msg_data["MessageInfo"]["MeetingWorker"]["MeetingDate"]["@xsi:nil"]
                    try:
                        meeting_worker.ballots_reception_end_date = msg_data["MessageInfo"]["MeetingWorker"]["BallotsReceptionEndDate"]
                    except:
                        pass
                    try:
                        meeting_worker.ballots_send_post_address = msg_data["MessageInfo"]["MeetingWorker"]["BallotsSendPostAddress"]
                    except:
                        pass
                    try:
                        meeting_worker.notice = msg_data["MessageInfo"]["MeetingWorker"]["Notice"]
                    except:
                        pass

                if message_info.message_type == "MeetingWorkerResult":
                    try:
                        meeting_worker_result.text = msg_data["MessageInfo"]["MeetingWorkerResult"]["Text"]
                    except:
                        pass
                    try:
                        meeting_worker_result.is_lead_by_arbitrmanager = json.loads(msg_data["MessageInfo"]["MeetingWorkerResult"]["IsLeadByArbitrManager"])
                    except:
                        pass
                    try:
                        meeting_worker_result.meeting_notice_date = \
                            msg_data["MessageInfo"]["MeetingWorkerResult"]["MeetingNoticeDate"]
                    except:
                        pass
                    else:
                        meeting_worker_result.meeting_notice_date = \
                            msg_data["MessageInfo"]["MeetingWorkerResult"]["MeetingNoticeDate"]["@xsi:nil"]
                    try:
                        meeting_worker_result.meeting_date = msg_data["MessageInfo"]["MeetingWorkerResult"]["MeetingDate"]
                    except:
                        pass
                    try:
                        meeting_worker_result.workers_count = msg_data["MessageInfo"]["MeetingWorkerResult"]["WorkersCount"]
                    except:
                        pass
                    try:
                        meeting_worker_result.requirement_summ = msg_data["MessageInfo"]["MeetingWorkerResult"]["RequirementSumm"]
                    except:
                        pass

                if message_info.message_type == "ViewDraftRestructuringPlan":
                    try:
                        view_draft_restructuring_plan.text = \
                            msg_data["MessageInfo"]["ViewDraftRestructuringPlan"]["Text"]
                    except:
                        pass
                    try:
                        view_draft_restructuring_plan.place_of_acquaintance = \
                            msg_data["MessageInfo"]["ViewDraftRestructuringPlan"]["PlaceOfAcquaintance"]
                    except:
                        pass
                    try:
                        view_draft_restructuring_plan.bankruptcy_acknowledgment_and_start_of_restructuring_messageid = \
                            msg_data["MessageInfo"]["ViewDraftRestructuringPlan"]["BankruptcyAcknowledgmentAndStartOfRestructuringMessageId"]
                    except:
                        pass

                if message_info.message_type == "ViewExecRestructuringPlan":
                    try:
                        view_exec_restructuring_plan.text = msg_data["MessageInfo"]["ViewExecRestructuringPlan"]["Text"]
                    except:
                        pass
                    try:
                        view_exec_restructuring_plan.date_end_restructuring_plan_execution = msg_data["MessageInfo"]["ViewExecRestructuringPlan"]["DateEndRestructuringPlanExecution"]
                    except:
                        pass
                    try:
                        view_exec_restructuring_plan.place_of_acquaintance = msg_data["MessageInfo"]["ViewExecRestructuringPlan"]["PlaceOfAcquaintance"]
                    except:
                        pass
                    try:
                        view_exec_restructuring_plan.included_registry_requirements_not_satisfied = json.loads(msg_data["MessageInfo"]["ViewExecRestructuringPlan"]["IncludedRegistryRequirmentsNotSatisfied"])
                    except:
                        pass

                if message_info.message_type == "TransferOwnershipRealEstate":
                    try:
                        transfer_ownership_real_estate.text = msg_data["MessageInfo"]["TransferOwnershipRealEstate"]["Text"]
                    except:
                        pass
                    try:
                        transfer_ownership_real_estate.court_decision_date = msg_data["MessageInfo"]["TransferOwnershipRealEstate"]["CourtDecisionDate"]
                    except:
                        pass
                    try:
                        transfer_ownership_real_estate.transfer_ownership_state_registration_date = msg_data["MessageInfo"]["TransferOwnershipRealEstate"]["TransferOwnershipStateRegistrationDate"]
                    except:
                        pass
                    try:
                        transfer_ownership_real_estate.acquirer_name = msg_data["MessageInfo"]["TransferOwnershipRealEstate"]["AcquirerName"]
                    except:
                        pass
                    try:
                        transfer_ownership_real_estate.acquirer_address = msg_data["MessageInfo"]["TransferOwnershipRealEstate"]["AcquirerAddress"]
                    except:
                        pass
                    try:
                        transfer_ownership_real_estate.acquirer_ogrn = msg_data["MessageInfo"]["TransferOwnershipRealEstate"]["AcquirerOgrn"]
                    except:
                        pass
                    try:
                        transfer_ownership_real_estate.acquirer_inn = msg_data["MessageInfo"]["TransferOwnershipRealEstate"]["AcquirerInn"]
                    except:
                        pass

                    #LandPlots -> LandPlot
                    try:
                        land_plot.cadastral_number = msg_data["MessageInfo"]["TransferOwnershipRealEstate"]["LandPlots"]["LandPlot"]["CadastralNumber"]
                    except:
                        pass
                    try:
                        land_plot.ownership_right_description = msg_data["MessageInfo"]["TransferOwnershipRealEstate"]["LandPlots"]["LandPlot"]["OwnershipRightDescription"]
                    except:
                        pass
                    try:
                        land_plot.additional_info = msg_data["MessageInfo"]["TransferOwnershipRealEstate"]["LandPlots"]["LandPlot"]["AdditionalInfo"]
                    except:
                        pass
                    try:
                        uncompleted_building_project.address = msg_data["MessageInfo"]["TransferOwnershipRealEstate"]["UncompletedBuildingProjects"]["UncompletedBuildingProject"]["Address"]
                    except:
                        pass
                    try:
                        uncompleted_building_project.cadastral_number = msg_data["MessageInfo"]["TransferOwnershipRealEstate"]["UncompletedBuildingProjects"]["UncompletedBuildingProject"]["CadastralNumber"]
                    except:
                        pass
                    try:
                        uncompleted_building_project.additional_info = msg_data["MessageInfo"]["TransferOwnershipRealEstate"]["UncompletedBuildingProjects"]["UncompletedBuildingProject"]["AdditionalInfo"]
                    except:
                        pass

                if message_info.message_type == "CancelAuctionTradeResult":
                    try:
                        cancel_auction_trade_result.text = msg_data["MessageInfo"]["CancelAuctionTradeResult"]["Text"]
                    except:
                        pass
                    try:
                        cancel_auction_trade_result.id_cancelled_message = msg_data["MessageInfo"]["CancelAuctionTradeResult"]["IdCanceledMessage"]
                    except:
                        pass
                    try:
                        cancel_auction_trade_result.cancellation_reason = msg_data["MessageInfo"]["CancelAuctionTradeResult"]["CancellationReason"]
                    except:
                        pass

                if message_info.message_type == "CancelDeliberateBankruptcy":
                    try:
                        cancel_deliberate_bankruptcy.text = msg_data["MessageInfo"]["CancelDeliberateBankruptcy"]["Text"]
                    except:
                        pass
                    try:
                        cancel_deliberate_bankruptcy.cancellation_reason = msg_data["MessageInfo"]["CancelDeliberateBankruptcy"]["CancellationReason"]
                    except:
                        pass
                    try:
                        cancel_deliberate_bankruptcy.id_changed_message = msg_data["MessageInfo"]["CancelDeliberateBankruptcy"]["IdChangedMessage"]
                    except:
                        pass

                if message_info.message_type == "ChangeAuction":
                    try:
                        change_auction.is_repeat = json.loads(msg_data["MessageInfo"]["ChangeAuction"]["IsRepeat"])
                    except:
                        pass
                    try:
                        change_auction.date = msg_data["MessageInfo"]["ChangeAuction"]["Date"]
                    except:
                        pass
                    try:
                        change_auction.id_changed_message = msg_data["MessageInfo"]["ChangeAuction"]["IdChangedMessage"]
                    except:
                        pass
                    try:
                        change_auction.change_reason = msg_data["MessageInfo"]["ChangeAuction"]["ChangeReason"]
                    except:
                        pass
                    try:
                        change_auction.trade_type = msg_data["MessageInfo"]["ChangeAuction"]["TradeType"]
                    except:
                        pass
                    try:
                        change_auction.price_type = msg_data["MessageInfo"]["ChangeAuction"]["PriceType"]
                    except:
                        pass
                    try:
                        change_auction.text = msg_data["MessageInfo"]["ChangeAuction"]["Text"]
                    except:
                        pass
                    try:
                        change_auction.trade_site = msg_data["MessageInfo"]["ChangeAuction"]["TradeSite"]
                    except:
                        pass
                    try:
                        change_auction.id_trade_place = msg_data["MessageInfo"]["ChangeAuction"]["IdTradePlace"]
                    except:
                        pass
                    try:
                        change_auction.additional_text = msg_data["MessageInfo"]["ChangeAuction"]["AdditionalText"]
                    except:
                        pass

                    # Application
                    try:
                        application.time_begin = msg_data["MessageInfo"]["ChangeAuction"]["Application"]["TimeBegin"]
                    except:
                        pass
                    try:
                        application.time_end = msg_data["MessageInfo"]["ChangeAuction"]["Application"]["TimeEnd"]
                    except:
                        pass
                    try:
                        application.rules = msg_data["MessageInfo"]["ChangeAuction"]["Application"]["Rules"]
                    except:
                        pass

                    # LotTable -> AuctionLot
                    try:
                        auction_lot.order = msg_data["MessageInfo"]["ChangeAuction"]["LotTable"]["AuctionLot"]["Order"]
                    except:
                        pass
                    try:
                        auction_lot.start_price = msg_data["MessageInfo"]["ChangeAuction"]["LotTable"]["AuctionLot"][
                            "StartPrice"]
                    except:
                        pass
                    try:
                        auction_lot.step = msg_data["MessageInfo"]["ChangeAuction"]["LotTable"]["AuctionLot"]["Step"]
                    except:
                        pass
                    try:
                        auction_lot.advance = msg_data["MessageInfo"]["ChangeAuction"]["LotTable"]["AuctionLot"]["Advance"]
                    except:
                        pass
                    try:
                        auction_lot.description = msg_data["MessageInfo"]["ChangeAuction"]["LotTable"]["AuctionLot"][
                            "Description"]
                    except:
                        pass
                    try:
                        auction_lot.auction_step_unit = msg_data["MessageInfo"]["ChangeAuction"]["LotTable"]["AuctionLot"][
                            "AuctionStepUnit"]
                    except:
                        pass
                    try:
                        auction_lot.advance_step_unit = msg_data["MessageInfo"]["ChangeAuction"]["LotTable"]["AuctionLot"][
                            "AdvanceStepUnit"]
                    except:
                        pass
                    try:
                        auction_lot.price_reduction = \
                            msg_data["MessageInfo"]["ChangeAuction"]["LotTable"]["AuctionLot"][
                                "PriceReduction"]
                    except:
                        pass
                        # classifierCollection
                    try:
                        auction_lot_classifier.code = \
                        msg_data["MessageInfo"]["ChangeAuction"]["LotTable"]["AuctionLot"]["ClassifierCollection"][
                            "AuctionLotClassifier"]["Code"]
                    except:
                        pass
                    try:
                        auction_lot_classifier.name = \
                        msg_data["MessageInfo"]["ChangeAuction"]["LotTable"]["AuctionLot"]["ClassifierCollection"][
                            "AuctionLotClassifier"]["Name"]
                    except:
                        pass

                if message_info.message_type == "ReducingSizeShareCapital":
                    try:
                        reducing_size_share_capital.text = msg_data["MessageInfo"]["ReducingSizeShareCapital"]["Text"]
                    except:
                        pass
                    try:
                        reducing_size_share_capital.charter_capital_sum = msg_data["MessageInfo"]["ReducingSizeShareCapital"]["CharterCapitalSum"]
                    except:
                        pass
                    try:
                        reducing_size_share_capital.normative_act_add_option_date = msg_data["MessageInfo"]["ReducingSizeShareCapital"]["NormativeActAdoptionDate"]
                    except:
                        pass
                    try:
                        reducing_size_share_capital.increase_capital_decision_cancelled = \
                            json.loads(msg_data["MessageInfo"]["ReducingSizeShareCapital"]["IncreaseCapitalDecisionCanceled"])
                    except:
                        pass

                if message_info.message_type == "SelectionPurchaserAssets":
                    try:
                        selection_purchaser_assets.text = msg_data["MessageInfo"]["SelectionPurchaserAssets"]["Text"]
                    except:
                        pass
    #
                if message_info.message_type == "EstimatesCurrentExpenses":
                    try:
                        estimates_current_expenses.text = msg_data["MessageInfo"]["EstimatesCurrentExpenses"]["Text"]
                    except:
                        pass
                if message_info.message_type == "OrderAndTimingCalculations":
                    try:
                        order_and_timing_calculations.text = msg_data["MessageInfo"]["OrderAndTimingCalculations"]["Text"]
                    except:
                        pass
                if message_info.message_type == "InformationAboutBankruptcy":
                    try:
                        information_about_bankruptcy.text = msg_data["MessageInfo"]["InformationAboutBankruptcy"]["Text"]
                    except:
                        pass
                if message_info.message_type == "EstimatesAndUnsoldAssets":
                    try:
                        estimates_and_unsold_assets.text = msg_data["MessageInfo"]["EstimatesAndUnsoldAssets"]["Text"]
                    except:
                        pass
                if message_info.message_type == "RemainingAssetsAndRight":
                    try:
                        remaining_assets_and_right.text = msg_data["MessageInfo"]["RemainingAssetsAndRight"]["Text"]
                    except:
                        pass
                if message_info.message_type == "ImpendingTransferAssets":
                    try:
                        impending_transfer_assets.text = msg_data["MessageInfo"]["ImpendingTransferAssets"]["Text"]
                    except:
                        pass
                    #CreditOrganizations
                    try:
                        credit_organization_info.name = msg_data["MessageInfo"]["ImpendingTransferAssets"]["CreditOrganizations"]["CreditOrganizationInfo"]["Name"]
                    except:
                        pass
                    try:
                        credit_organization_info.address = msg_data["MessageInfo"]["ImpendingTransferAssets"]["CreditOrganizations"]["CreditOrganizationInfo"]["Address"]
                    except:
                        pass
                    try:
                        credit_organization_info.ogrn = msg_data["MessageInfo"]["ImpendingTransferAssets"]["CreditOrganizations"]["CreditOrganizationInfo"]["Ogrn"]
                    except:
                        pass
                    try:
                        credit_organization_info.inn = msg_data["MessageInfo"]["ImpendingTransferAssets"]["CreditOrganizations"]["CreditOrganizationInfo"]["Inn"]
                    except:
                        pass
                    try:
                        credit_organization_info.acquirer_liabilities_classification_criteria = msg_data["MessageInfo"]["ImpendingTransferAssets"]["CreditOrganizations"]["CreditOrganizationInfo"]["AcquirerLiabilitiesClassificationCriteria"]
                    except:
                        pass
                    try:
                        credit_organization_info.transferred_liabilities_obtaining_order = msg_data["MessageInfo"]["ImpendingTransferAssets"]["CreditOrganizations"]["CreditOrganizationInfo"]["TransferredLiabilitiesObtainingOrder"]
                    except:
                        pass
                if message_info.message_type == "TransferAssets":
                    try:
                        impending_transfer_assets.text = msg_data["MessageInfo"]["TransferAssets"]["Text"]
                    except:
                        pass
                    # CreditOrganizations
                    try:
                        credit_organization_info.name = \
                        msg_data["MessageInfo"]["TransferAssets"]["CreditOrganizations"]["CreditOrganizationInfo"][
                            "Name"]
                    except:
                        pass
                    try:
                        credit_organization_info.address = \
                        msg_data["MessageInfo"]["TransferAssets"]["CreditOrganizations"]["CreditOrganizationInfo"][
                            "Address"]
                    except:
                        pass
                    try:
                        credit_organization_info.ogrn = \
                        msg_data["MessageInfo"]["TransferAssets"]["CreditOrganizations"]["CreditOrganizationInfo"][
                            "Ogrn"]
                    except:
                        pass
                    try:
                        credit_organization_info.inn = \
                        msg_data["MessageInfo"]["TransferAssets"]["CreditOrganizations"]["CreditOrganizationInfo"][
                            "Inn"]
                    except:
                        pass
                    try:
                        credit_organization_info.acquirer_liabilities_classification_criteria = \
                        msg_data["MessageInfo"]["TransferAssets"]["CreditOrganizations"]["CreditOrganizationInfo"][
                            "AcquirerLiabilitiesClassificationCriteria"]
                    except:
                        pass
                    try:
                        credit_organization_info.transferred_liabilities_obtaining_order = \
                        msg_data["MessageInfo"]["TransferAssets"]["CreditOrganizations"]["CreditOrganizationInfo"][
                            "TransferredLiabilitiesObtainingOrder"]
                    except:
                        pass

                if message_info.message_type == "TransferInsurancePortfolio":
                    try:
                        transfer_insurance_portfolio.text = msg_data["MessageInfo"]["TransferInsurancePortfolio"]["Text"]
                    except:
                        pass
                    try:
                        transfer_insurance_portfolio.expected_delivery_date = msg_data["MessageInfo"]["TransferInsurancePortfolio"]["ExpectedDeliveryDate"]
                    except:
                        pass
                    try:
                        transfer_insurance_portfolio.portfolio_transfer_reason = msg_data["MessageInfo"]["TransferInsurancePortfolio"]["PortfolioTransferReason"]
                    except:
                        pass
                    try:
                        transfer_insurance_portfolio.authority_limitation_info = msg_data["MessageInfo"]["TransferInsurancePortfolio"]["AuthorityLimitationInfo"]
                    except:
                        pass

                        #insurance organizations
                    try:
                        insurance_organization.name = \
                        msg_data["MessageInfo"]["TransferInsurancePortfolio"]["InsuranceOrganization"]["Name"]
                    except:
                        pass
                    try:
                        insurance_organization.address = \
                        msg_data["MessageInfo"]["TransferInsurancePortfolio"]["InsuranceOrganization"]["Address"]
                    except:
                        pass
                    try:
                        insurance_organization.ogrn = \
                        msg_data["MessageInfo"]["TransferInsurancePortfolio"]["InsuranceOrganization"]["Ogrn"]
                    except:
                        pass
                    try:
                        insurance_organization.inn = \
                        msg_data["MessageInfo"]["TransferInsurancePortfolio"]["InsuranceOrganization"]["Inn"]
                    except:
                        pass

                if message_info.message_type == "BankOpenAccountDebtor":
                    try:
                        bank_open_account_debtor.text = msg_data["MessageInfo"]["BankOpenAccountDebtor"]["Text"]
                    except:
                        pass
                    try:
                        bank_open_account_debtor.name = msg_data["MessageInfo"]["BankOpenAccountDebtor"]["Name"]
                    except:
                        pass
                    try:
                        bank_open_account_debtor.inn = msg_data["MessageInfo"]["BankOpenAccountDebtor"]["Inn"]
                    except:
                        pass
                    try:
                        bank_open_account_debtor.ogrn = msg_data["MessageInfo"]["BankOpenAccountDebtor"]["Ogrn"]
                    except:
                        pass
                    try:
                        bank_open_account_debtor.bik = msg_data["MessageInfo"]["BankOpenAccountDebtor"]["Bik"]
                    except:
                        pass

                if message_info.message_type == "ProcedureGrantingIndemnity":
                    try:
                        procedure_granting_indemnity.text = msg_data["MessageInfo"]["ProcedureGrantingIndemnity"]["Text"]
                    except:
                        pass
                    try:
                        procedure_granting_indemnity.property_indemnity_offer = msg_data["MessageInfo"]["ProcedureGrantingIndemnity"]["PropertyIndemnityOffer"]
                    except:
                        pass
                    try:
                        procedure_granting_indemnity.property_familiarization_procedure = msg_data["MessageInfo"]["ProcedureGrantingIndemnity"]["PropertyFamiliarizationProcedure"]
                    except:
                        pass
                    try:
                        procedure_granting_indemnity.consest_application_period = msg_data["MessageInfo"]["ProcedureGrantingIndemnity"]["ConsestApplicationPeriod"]
                    except:
                        pass

                if message_info.message_type == "RightUnsoldAsset":
                    try:
                        right_unsold_asset.text = msg_data["MessageInfo"]["RightUnsoldAsset"]["Text"]
                    except:
                        pass

                if message_info.message_type == "TransferResponsibilitiesFund":
                    try:
                        transfer_responsibilities_fund.text = msg_data["MessageInfo"]["RightUnsoldAsset"]["Text"]
                    except:
                        pass

                if message_info.message_type == "ExtensionAdministration":
                    try:
                        extension_administration.text = msg_data["MessageInfo"]["ExtensionAdministration"]["Text"]
                    except:
                        pass
                #

                if message_info.message_type == "MeetingParticipantsBuilding":
                    try:
                        meeting_participants_building.text = msg_data["MessageInfo"]["MeetingParticipantsBuilding"]["Text"]
                    except:
                        pass
                    try:
                        meeting_participants_building.meeting_date = msg_data["MessageInfo"]["MeetingParticipantsBuilding"]["MeetingDate"]
                    except:
                        pass
                    try:
                        meeting_participants_building.meeting_site = msg_data["MessageInfo"]["MeetingParticipantsBuilding"]["MeetingSite"]
                    except:
                        pass
                    try:
                        meeting_participants_building.notice = msg_data["MessageInfo"]["MeetingParticipantsBuilding"]["Notice"]
                    except:
                        pass
                    try:
                        meeting_participants_building.materials_familiarization_order = msg_data["MessageInfo"]["MeetingParticipantsBuilding"]["MaterialsFamiliarizationOrder"]
                    except:
                        pass

                if message_info.message_type == "MeetingPartBuildResult":
                    try:
                        meeting_part_build_result.text = msg_data["MessageInfo"]["MeetingPartBuildResult"]["Text"]
                    except:
                        pass

                if message_info.message_type == "PartBuildMonetaryClaim":
                    try:
                        part_build_monetary_claim.text = msg_data["MessageInfo"]["PartBuildMonetaryClaim"]["Text"]
                    except:
                        pass
                    try:
                        part_build_monetary_claim.arbitral_court = msg_data["MessageInfo"]["PartBuildMonetaryClaim"]["ArbitralCourt"]
                    except:
                        pass
                    try:
                        part_build_monetary_claim.consequences = msg_data["MessageInfo"]["PartBuildMonetaryClaim"]["Consequences"]
                    except:
                        pass

                if message_info.message_type == "StartSettlement":
                    try:
                        start_settlement.text = msg_data["MessageInfo"]["StartSettlement"]["Text"]
                    except:
                        pass
                    try:
                        start_settlement.settlement_start_date = msg_data["MessageInfo"]["StartSettlement"]["SettlementStartDate"]
                    except:
                        pass

                if message_info.message_type == "ProcessInventoryDebtor":
                    try:
                        process_inventory_debtor.text = msg_data["MessageInfo"]["ProcessInventoryDebtor"]["Text"]
                    except:
                        pass

                if message_info.message_type == "Rebuttal":
                    try:
                        rebuttal.text = msg_data["MessageInfo"]["Rebuttal"]["Text"]
                    except:
                        pass
                    try:
                        rebuttal.id_rebutted_message = msg_data["MessageInfo"]["Rebuttal"]["IdRebuttedMessage"]
                    except:
                        pass

                if message_info.message_type == "CreditorChoiceRightSubsidiary":
                    try:
                        creditor_choice_right_subsidiary.text = msg_data["MessageInfo"]["CreditorChoiceRightSubsidiary"]["Text"]
                    except:
                        pass
                    try:
                        creditor_choice_right_subsidiary.subsidiary_message_id = msg_data["MessageInfo"]["CreditorChoiceRightSubsidiary"]["SubsidiaryMessageId"]
                    except:
                        pass
                    try:
                        creditor_choice_right_subsidiary.subsidiary_act_date = msg_data["MessageInfo"]["CreditorChoiceRightSubsidiary"]["SubsidiaryActDate"]
                    except:
                        pass
    ##
                if message_info.message_type == "AccessionDeclarationSubsidiary":
                    try:
                        accession_declaration_subsidiary.text = msg_data["MessageInfo"]["AccessionDeclarationSubsidiary"]["Text"]
                    except:
                        pass
                    try:
                        accession_declaration_subsidiary.declaration_person_subsidiary_message_id = msg_data["MessageInfo"]["AccessionDeclarationSubsidiary"]["DeclarationPersonSubsidiaryMessageId"]
                    except:
                        pass
                if message_info.message_type == "DisqualificationArbitrationManager":
                    try:
                        disqualification_arbitration_manager.text = msg_data["MessageInfo"]["DisqualificationArbitrationManager"]["Text"]
                    except:
                        pass
                    try:
                        disqualification_arbitration_manager.duration = msg_data["MessageInfo"]["DisqualificationArbitrationManager"]["Duration"]
                    except:
                        pass
                    try:
                        disqualification_arbitration_manager.reason = msg_data["MessageInfo"]["DisqualificationArbitrationManager"]["Reason"]
                    except:
                        pass

                    #arbitr
                    try:
                        arbitr_manager.snils = msg_data["MessageInfo"]["DisqualificationArbitrationManager"]["ArbitrManager"]["Snils"]
                    except:
                        pass
                    try:
                        arbitr_manager.inn = msg_data["MessageInfo"]["DisqualificationArbitrationManager"]["ArbitrManager"]["Inn"]
                    except:
                        pass
                    try:
                        arbitr_manager.fio = msg_data["MessageInfo"]["DisqualificationArbitrationManager"]["ArbitrManager"]["Fio"]
                    except:
                        pass
                    try:
                        court.name = msg_data["MessageInfo"]["DisqualificationArbitrationManager"]["Court"]["Name"]
                        court.name = msg_data["MessageInfo"]["DisqualificationArbitrationManager"]["Court"]["Name"]
                    except:
                        pass

                if message_info.message_type == "DisqualificationArbitrationManager2":
                    try:
                        disqualification_arbitration_manager2.text = msg_data["MessageInfo"]["DisqualificationArbitrationManager2"][
                            "Text"]
                    except:
                        pass
                    try:
                        disqualification_arbitration_manager2.reason = msg_data["MessageInfo"]["DisqualificationArbitrationManager2"][
                            "Reason"]
                    except:
                        pass

                        # arbitr
                    try:
                        arbitr_manager.snils = msg_data["MessageInfo"]["DisqualificationArbitrationManager2"]["ArbitrManager"]["Snils"]
                    except:
                        pass
                    try:
                        arbitr_manager.inn = msg_data["MessageInfo"]["DisqualificationArbitrationManager2"]["ArbitrManager"]["Inn"]
                    except:
                        pass
                    try:
                        arbitr_manager.fio = msg_data["MessageInfo"]["DisqualificationArbitrationManager2"]["ArbitrManager"]["Fio"]
                    except:
                        pass

                    try:
                        court.name = msg_data["MessageInfo"]["DisqualificationArbitrationManager2"]["Court"]["Name"]
                        court.name = msg_data["MessageInfo"]["DisqualificationArbitrationManager2"]["Court"]["Name"]
                    except:
                        pass
                    try:
                        duration.year = msg_data["MessageInfo"]["DisqualificationArbitrationManager2"]["Duration"]["Year"]
                    except:
                        pass
                    try:
                        duration.month = msg_data["MessageInfo"]["DisqualificationArbitrationManager2"]["Duration"]["Month"]
                    except:
                        pass
                    try:
                        duration.day = msg_data["MessageInfo"]["DisqualificationArbitrationManager2"]["Duration"]["Day"]
                    except:
                        pass

                if message_info.message_type == "ChangeEstimatesCurrentExpenses":
                    try:
                        change_estimates_current_expenses.text =  msg_data["MessageInfo"]["ChangeEstimatesCurrentExpenses"][
                            "Text"]
                    except:
                        pass
                    try:
                        change_estimates_current_expenses.id_changed_message = msg_data["MessageInfo"]["ChangeEstimatesCurrentExpenses"][
                            "IdChangedMessage"]
                    except:
                        pass
                if message_info.message_type == "ActPersonSubsidiary2":
                    try:
                        act_person_subsidiary2.text = msg_data["MessageInfo"]["ActPersonSubsidiary2"][
                            "Text"]
                    except:
                        pass
                    try:
                        message.number = msg_data["MessageInfo"]["ActPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"]["Message"]["Number"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.bankrupt_supervisory_person = msg_data["MessageInfo"]["ActPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"]["Message"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["@xsi:type"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.responsibility_amount =  msg_data["MessageInfo"]["ActPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"]["Message"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["ResponsibilityAmount"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.name =  msg_data["MessageInfo"][
                            "ActPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"][
                            "Message"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Name"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code =  msg_data["MessageInfo"]["ActPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"]["Message"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Code"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code_type = \
                        msg_data["MessageInfo"]["ActPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"]["Message"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["CodeType"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.country =  msg_data["MessageInfo"]["ActPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"]["Message"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["CodeType"]
                    except:
                        pass

                if message_info.message_type == "ActReviewPersonSubsidiary2":
                    try:
                        act_review_person_subsidiary2.text =  msg_data["MessageInfo"]["ActReviewPersonSubsidiary2"][
                            "Text"]
                    except:
                        pass
                    try:
                        message.number = msg_data["MessageInfo"]["ActReviewPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"]["Message"]["Number"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.bankrupt_supervisory_person = msg_data["MessageInfo"]["ActReviewPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"]["Message"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["@xsi:type"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.responsibility_amount =  msg_data["MessageInfo"]["ActReviewPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"]["Message"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["ResponsibilityAmount"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.name =  msg_data["MessageInfo"][
                            "ActReviewPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"][
                            "Message"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Name"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code =  msg_data["MessageInfo"]["ActReviewPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"]["Message"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["Code"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.code_type = \
                        msg_data["MessageInfo"]["ActReviewPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"]["Message"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["CodeType"]
                    except:
                        pass
                    try:
                        bankrupt_supervisory_person.country =  msg_data["MessageInfo"]["ActReviewPersonSubsidiary2"]["DeclarationPersonSubsidiaryInfoMessages"]["Message"]["BankruptSupervisoryPersons"]["BankruptSupervisoryPerson"]["CodeType"]
                    except:
                        pass

                if message_info.message_type == "AssessmentReport":
                    assessment_report.text = msg_data["MessageInfo"]["AssessmentReport"]["Text"]
                    try:
                    #report
                        assessment_report.reason = msg_data["MessageInfo"]["AssessmentReport"]["Reason"]
                    except:
                        pass
                    try:
                    #report
                        report.number = msg_data["MessageInfo"]["AssessmentReport"]["Report"]["Number"]
                        report.date = msg_data["MessageInfo"]["AssessmentReport"]["Report"]["Date"]
                    except:
                        pass
                    #appraisers -> appraiser
                    try:
                        appraiser.inn = msg_data["MessageInfo"]["AssessmentReport"]["Appraisers"]["Appraiser"]["Inn"]
                        appraiser.snils = msg_data["MessageInfo"]["AssessmentReport"]["Appraisers"]["Appraiser"]["Inn"]
                    except:
                        pass
                    #sro
                    try:
                        sro.name = msg_data["MessageInfo"]["AssessmentReport"]["Appraisers"]["Appraiser"]["Sro"]["Name"]
                        sro.inn = msg_data["MessageInfo"]["AssessmentReport"]["Appraisers"]["Appraiser"]["Sro"]["Inn"]
                        sro.ogrn = msg_data["MessageInfo"]["AssessmentReport"]["Appraisers"]["Appraiser"]["Sro"]["Ogrn"]
                    except:
                        pass

                    #fio
                    try:
                        fio.first_name = msg_data["MessageInfo"]["AssessmentReport"]["Appraisers"]["Appraiser"]["Fio"]["FirstName"]
                        fio.last_name = msg_data["MessageInfo"]["AssessmentReport"]["Appraisers"]["Appraiser"]["Fio"]["LastName"]
                        fio.middle_name = msg_data["MessageInfo"]["AssessmentReport"]["Appraisers"]["Appraiser"]["Fio"]["MiddleName"]
                    except:
                        pass
                    #objects of assesment
                    try:
                        object_of_assessment.description = msg_data["MessageInfo"]["AssessmentReport"]["ObjectsOfAssessment"][
                        "ObjectOfAssessment"]["Description"]
                        object_of_assessment.date_of_assessment = msg_data["MessageInfo"]["AssessmentReport"]["ObjectsOfAssessment"][
                            "ObjectOfAssessment"]["DateOfAssessment"]
                        object_of_assessment.market_value = msg_data["MessageInfo"]["AssessmentReport"]["ObjectsOfAssessment"][
                            "ObjectOfAssessment"]["MarketValue"]
                        object_of_assessment.balance_value = msg_data["MessageInfo"]["AssessmentReport"]["ObjectsOfAssessment"][
                            "ObjectOfAssessment"]["BalanceValue"]
                        #classifier
                        classifier.code = msg_data["MessageInfo"]["AssessmentReport"]["ObjectsOfAssessment"][
                        "ObjectOfAssessment"]["Classifier"]["Code"]
                        classifier.name = msg_data["MessageInfo"]["AssessmentReport"]["ObjectsOfAssessment"][
                            "ObjectOfAssessment"]["Classifier"]["Name"]
                        #ExpertDecision
                        expert_decision.number = msg_data["MessageInfo"]["AssessmentReport"]["ExpertDecision"]["Number"]
                    except:
                        pass
                    try:
                        expert_decision.date = msg_data["MessageInfo"]["AssessmentReport"]["ExpertDecision"]["Date"]
                    except:
                        pass
                    else:
                        expert_decision.date = msg_data["MessageInfo"]["AssessmentReport"]["ExpertDecision"]["Date"]["@xsi:nil"]
                    try:
                        expert_decision.result = msg_data["MessageInfo"]["AssessmentReport"]["ExpertDecision"]["Result"]
                    except:
                        pass
                    #expert
                    try:
                        expert.innn = msg_data["MessageInfo"]["AssessmentReport"]["ExpertDecision"]["Experts"]["Expert"]["Inn"]
                        expert.snils = \
                        msg_data["MessageInfo"]["AssessmentReport"]["ExpertDecision"]["Experts"]["Expert"]["Snils"]
                        #sro
                        sro.name = msg_data["MessageInfo"]["AssessmentReport"]["ExpertDecision"]["Experts"]["Expert"]["Sro"]["Name"]
                        sro.ogrn = msg_data["MessageInfo"]["AssessmentReport"]["ExpertDecision"]["Experts"]["Expert"]["Sro"][
                            "Ogrn"]
                        sro.name = msg_data["MessageInfo"]["AssessmentReport"]["ExpertDecision"]["Experts"]["Expert"]["Sro"]["Inn"]
                        #fio
                        fio.first_name = msg_data["MessageInfo"]["AssessmentReport"]["ExpertDecision"]["Experts"]["Expert"]["Fio"][
                        "FirstName"]
                        fio.last_name = \
                        msg_data["MessageInfo"]["AssessmentReport"]["ExpertDecision"]["Experts"]["Expert"]["Fio"][
                        "LastName"]
                        fio.middle_name = msg_data["MessageInfo"]["AssessmentReport"]["ExpertDecision"]["Experts"]["Expert"]["Fio"][
                        "MiddleName"]
                    except:
                        pass
                if message_info.message_type == "ReturnOfApplicationOnExtrajudicialBankruptcy":
                    try:
                        return_of_application_on_extrajudicial_bankruptcy.date =  msg_data["MessageInfo"][
                            "ReturnOfApplicationOnExtrajudicialBankruptcy"]["Date"]
                    except:
                        pass
                    try:
                        return_of_application_on_extrajudicial_bankruptcy.no_return_of_enforcement_documen = json.loads(msg_data["MessageInfo"][
                            "ReturnOfApplicationOnExtrajudicialBankruptcy"]["NoReturnOfEnforcementDocumen"])
                    except:
                        pass
                    try:
                        return_of_application_on_extrajudicial_bankruptcy.active_enforcement_proceeding = json.loads(msg_data["MessageInfo"][
                            "ReturnOfApplicationOnExtrajudicialBankruptcy"]["ActiveEnforcementProceeding"])
                    except:
                        pass
                #!
                if message_info.message_type == "StartOfExtrajudicialBankruptcy":
                    try:
                        start_of_extrajudicial_bankruptcy.is_individual_entrepreneur = json.loads(msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"]["IsIndividualEntrepreneur"])
                        #CreditorsFromEntrepreneurship
                        creditors_from_entrepreneurship.non_monetary_obligations = \
                            json.loads(msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"]["CreditorsFromEntrepreneurship"]["NonMonetaryObligations"])
                        #MonetaryObligations
                        monetary_obligation.creditor_name = msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"][
                            "CreditorsFromEntrepreneurship"]["MonetaryObligations"]["MonetaryObligation"]["CreditorName"]
                        monetary_obligation.creditor_region = msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"][
                            "CreditorsFromEntrepreneurship"]["MonetaryObligations"]["MonetaryObligation"]["CreditorRegion"]
                        monetary_obligation.creditor_location = msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"][
                            "CreditorsFromEntrepreneurship"]["MonetaryObligations"]["MonetaryObligation"]["CreditorLocation"]
                        monetary_obligation.content = msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"][
                            "CreditorsFromEntrepreneurship"]["MonetaryObligations"]["MonetaryObligation"]["Content"]
                        monetary_obligation.basis = msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"][
                            "CreditorsFromEntrepreneurship"]["MonetaryObligations"]["MonetaryObligation"]["Basis"]
                        monetary_obligation.total_sum = msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"][
                            "CreditorsFromEntrepreneurship"]["MonetaryObligations"]["MonetaryObligation"]["TotalSum"]
                        monetary_obligation.debt_sum = msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"][
                            "CreditorsFromEntrepreneurship"]["MonetaryObligations"]["MonetaryObligation"]["DebtSum"]
                        monetary_obligation.penalty_sum = msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"][
                            "CreditorsFromEntrepreneurship"]["MonetaryObligations"]["MonetaryObligation"]["PenaltySum"]
                        #ObligatoryPayment
                        obligatory_payment.name = msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"][
                            "CreditorsFromEntrepreneurship"]["ObligatoryPayments"]["ObligatoryPayment"]["Name"]
                        obligatory_payment.sum = msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"][
                            "CreditorsFromEntrepreneurship"]["ObligatoryPayments"]["ObligatoryPayment"]["Sum"]
                        obligatory_payment.penalty_sum = msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"][
                            "CreditorsFromEntrepreneurship"]["ObligatoryPayments"]["ObligatoryPayment"]["PenaltySum"]
                        #banks
                        bank.name = msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"][
                            "Banks"]["Bank"]["Name"]
                        bank.bank_identifier =  msg_data["MessageInfo"]["StartOfExtrajudicialBankruptcy"][
                            "Banks"]["Bank"]["BankIdentifier"]
                    except:
                        pass

                if message_info.message_type == "TerminationOfExtrajudicialBankruptcy":

                    try:
                        termination_of_extrajudicial_bankruptcy.start_of_extrajudicial_bankruptcy_message_number = \
                            msg_data["MessageInfo"][
                                "TerminationOfExtrajudicialBankruptcy"]["StartOfExtrajudicialBankruptcyMessageNumber"]
                    except:
                        pass
                    try:
                        termination_of_extrajudicial_bankruptcy.property_status_changed = \
                            json.loads(msg_data["MessageInfo"][
                                "TerminationOfExtrajudicialBankruptcy"]["PropertyStatusChanged"])
                    except:
                        pass
                    try:
                        termination_of_extrajudicial_bankruptcy.court_decision_issued = \
                            json.loads(msg_data["MessageInfo"][
                                           "TerminationOfExtrajudicialBankruptcy"]["CourtDecisionIssued"])
                    except:
                        pass
                    try:
                        termination_of_extrajudicial_bankruptcy.other_reason = \
                            msg_data["MessageInfo"][
                                "TerminationOfExtrajudicialBankruptcy"]["OtherReason"]
                    except:
                        pass

                if message_info.message_type == "CompletionOfExtrajudicialBankruptcy":
                    try:
                        completion_of_extrajudicial_bankruptcy.text = msg_data["MessageInfo"][
                            "CompletionOfExtrajudicialBankruptcy"]["Text"]
                    except:
                        pass
                    try:
                        completion_of_extrajudicial_bankruptcy.start_of_extrajudicial_bankruptcy_message_number = msg_data["MessageInfo"][
                            "CompletionOfExtrajudicialBankruptcy"]["StartOfExtrajudicialBankruptcyMessageNumber"]
                    except:
                        pass

                #bankrupt
                bankrupt_type = msg_data["Bankrupt"]["@xsi:type"]
                # bankrupt_info.bankrupt_type = bankrupt_type
                bankrupt.bankrupt = bankrupt_type
                # #print(bankrupt_type)
                if bankrupt_type == "Bankrupt.Company.v2":
                    try:
                        bankrupt_company_v2.name =  msg_data["Bankrupt"]["Name"]
                    except:
                        pass
                    try:
                        bankrupt_company_v2.ogrn =  msg_data["Bankrupt"]["Ogrn"]
                    except:
                        pass
                    try:
                        bankrupt_company_v2.inn =  msg_data["Bankrupt"]["Inn"]
                    except:
                        pass
                    try:
                        bankrupt_company_v2.address =  msg_data["Bankrupt"]["Address"]
                    except:
                        pass
                        #category
                    try:
                        category.code = msg_data["Bankrupt"]["Category"]["Code"]
                    except:
                        pass
                    try:
                        category.description = msg_data["Bankrupt"]["Category"]["Description"]
                    except:
                        pass

                if bankrupt_type == "Bankrupt.Person.v2":
                    try:
                        bankrupt_person_v2.inn =  msg_data["Bankrupt"]["Inn"]
                    except:
                        pass
                    try:
                        bankrupt_person_v2.ogrnip =  msg_data["Bankrupt"]["Ogrnip"]
                    except:
                        pass
                    try:
                        bankrupt_person_v2.snils =  msg_data["Bankrupt"]["Snils"]
                    except:
                        pass
                    try:
                        bankrupt_person_v2.address =  msg_data["Bankrupt"]["Address"]
                    except:
                        pass
                    try:
                        bankrupt_person_v2.birth_date =  msg_data["Bankrupt"]["Birthdate"]
                    except:
                        pass
                    try:
                        bankrupt_person_v2.birth_place =  msg_data["Bankrupt"]["Birthplace"]
                    except:
                        pass
                    try:
                        bankrupt_person_v2.inn = msg_data["Bankrupt"]["Inn"]
                    except:
                        pass

                    # category
                    try:
                        category.code = msg_data["Bankrupt"]["Category"]["Code"]
                        category.description = msg_data["Bankrupt"]["Category"]["Description"]
                    except:
                        pass
                    #Fio
                    try:
                        fio.last_name = msg_data["Bankrupt"]["Fio"]["LastName"]
                        fio.first_name = msg_data["Bankrupt"]["Fio"]["FirstName"]
                        fio.middle_name = msg_data["Bankrupt"]["Fio"]["MiddleName"]
                    except:
                        pass

                    # fio_history.fio = fio

                try:
                    message_data.message_guid = msg_data["MessageGUID"]
                except:
                    pass
                try:
                    message_data.publish_date = msg_data["PublishDate"]
                except:
                    pass
                try:
                    message_data.bankruptid = msg_data["BankruptId"]
                except:
                    pass
                try:
                    file_info.name = msg_data["FileInfoList"]["FileInfo"]["Name"]
                    file_info.hash = msg_data["FileInfoList"]["FileInfo"]["Hash"]
                except Exception as ex:
                    pass
                else:
                    try:
                        file_info.name = msg_data["FileInfoList"]["FileInfo"][0]["Name"]
                        file_info.hash = msg_data["FileInfoList"]["FileInfo"][0]["Hash"]
                    except Exception as ex:
                        pass
                #################################################################################
                #Saving
                try:
                    if file_info.name is not None:
                        file_info.save()
                        file_info_list.file_info = file_info
                        file_info_list.save()
                        message_data.file_info_list = file_info_list
                except:
                    pass
                try:
                    if sro:
                        sro.save()
                except:
                    pass
                # try:
                #     if publisher_arbitr_manager_v2:
                #         if sro.name is not None or sro.ogrn is not None:
                #             sro.save()
                #             publisher_arbitr_manager_v2.sro = sro
                #         if fio.first_name is not None or fio.last_name is not None:
                #             fio.save()
                #             publisher_arbitr_manager_v2.fio = fio
                #         publisher_arbitr_manager_v2.save()
                # except Exception as ex:
                #     pass
                try:
                    if publisher:
                        publisher.xsi_type = xsi_type
                        if publisher_arbitr_manager_v2.inn is not None or publisher_arbitr_manager_v2.snils is not None :
                            if sro.name is not None or sro.ogrn is not None:
                                sro.save()
                                publisher_arbitr_manager_v2.sro = sro
                            if fio.first_name is not None or fio.last_name is not None:
                                fio.save()
                                publisher_arbitr_manager_v2.fio = fio
                            publisher_arbitr_manager_v2.save()
                            publisher.publisher_arbitr_manager_v2 = publisher_arbitr_manager_v2
                        if publisher_arbitr_manager_sro_v2.name is not None:
                            publisher_arbitr_manager_sro_v2.save()
                            publisher.publisher_arbitr_manager_sro_v2 = publisher_arbitr_manager_sro_v2
                        if publisher_firmtrade_organizer_v2.name is not None:
                            publisher_firmtrade_organizer_v2.save()
                            publisher.publisher_firmtrade_organizer_v2 = publisher_firmtrade_organizer_v2
                        if publisher_persontrade_organizer_v2.pk is not None:
                            if fio.first_name is not None or fio.last_name is not None:
                                fio.save()
                                publisher_persontrade_organizer_v2.fio = fio
                            publisher_persontrade_organizer_v2.save()
                            publisher.publisher_persontrade_organizer_v2 = publisher_persontrade_organizer_v2
                        if publisher_company_v2.name is not None:
                            publisher_company_v2.save()
                        if publisher_person_v2.inn is not None:
                            publisher_person_v2.save()
                            publisher.publisher_person_v2 = publisher_person_v2
                        if publisher_centralbankrf_v2.name is not None:
                            publisher_centralbankrf_v2.save()
                            publisher.publisher_centralbankrf_v2 = publisher_centralbankrf_v2
                        if publisher_asv_v2.name is not None:
                            publisher_asv_v2.save()
                            publisher.publisher_asv_v2 = publisher_asv_v2
                        if publisher_fnsdepartment_v2.name is not None:
                            publisher_fnsdepartment_v2.save()
                            publisher.publisher_fnsdepartment_v2 = publisher_fnsdepartment_v2
                        if publisher_efrsb_v2.name is not None:
                            publisher_efrsb_v2.save()
                            publisher.publisher_efrsb_v2 = publisher_efrsb_v2
                        if publisher_mfc_v2.name is not None:
                            publisher_mfc_v2.save()
                            publisher.publisher_mfc_v2 = publisher_mfc_v2
                        publisher.save()
                except Exception as ex:
                    pass


                try:
                    if bankrupt:
                        if bankrupt_person_v2.snils is not None:
                            if fio.first_name is not None:
                                fio.save()
                                fio_history.fio = fio
                                fio_history.save()
                                bankrupt_person_v2.fio = fio
                                bankrupt_person_v2.fio_history = fio_history

                            if category.code is not None:
                                category.save()
                                bankrupt_person_v2.category = category
                            bankrupt_person_v2.save()

                            bankrupt.bankrupt_person_v2 = bankrupt_person_v2

                        if bankrupt_company_v2.name is not None:
                            if category.code is not None:
                                category.save()
                                bankrupt_company_v2.category = category
                            bankrupt_company_v2.save()
                            bankrupt.bankrupt_company_v2 = bankrupt_company_v2
                        bankrupt.save()
                        message_data.bankrupt = bankrupt
                except Exception as ex:
                    pass
                try:
                    if message_info.message_type is not None:
                        if court_decision.text is not None:
                            court_decision.save()
                            message_types.arbitral_decree = court_decision
                        if auction.text is not None:
                            if auction_lot_classifier.name is not None:
                                auction_lot_classifier.save()
                            if application.rules is not None:
                                application.save()
                                auction.application = application
                            if auction_lot.order is not None:
                                if auction_lot_classifier.name is not None:
                                    auction_lot_classifier.save()
                                    auction_lot.classifier_collection = auction_lot_classifier
                                auction_lot.save()
                                lot_table.auction_lot = auction_lot
                                lot_table.save()
                                auction.lot_table = lot_table
                            auction.save()
                            message_types.auction = auction
                        try:
                            if meeting.text is not None:
                                # if auction.text is not None:
                                #     auction.save()
                                #     meeting.auction = auction
                                meeting.save()
                                message_types.meeting = meeting
                        except Exception as ex:
                            pass
                            # exit()
                        if meeting_result.text is not None:
                            meeting_result.save()
                            message_types.meeting_result = meeting_result
                        try:
                            if trade_result.text is not None:
                                if trade_result_lot.order is not None:
                                    if auction_lot_classifier.name is not None:
                                        auction_lot_classifier.save()
                                        trade_result_lot.classifier_collection = auction_lot_classifier
                                    if participant_person.price_offer is not None:
                                        participant_person.save()
                                        if status == "winner":
                                            winner.participant_person = participant_person
                                            winner.save()
                                            trade_result_lot.winner = winner

                                    if participant_company.price_offer is not None:
                                        participant_company.save()
                                        if status == "winner":
                                            winner.participant_company = participant_company
                                            winner.save()
                                            trade_result_lot.winner = winner
                                    trade_result_lot.save()

                                    if participant_person.price_offer is not None:
                                        participant_person.save()
                                        if status == "buyer":
                                            buyer.participant_person = participant_person
                                            buyer.save()
                                            trade_result_lot.buyer = buyer

                                    if participant_company.price_offer is not None:
                                        participant_company.save()
                                        if status == "buyer":
                                            buyer.participant_company = participant_company
                                            buyer.save()
                                            trade_result_lot.buyer = buyer
                                    trade_result_lot.save()

                                    # lot_table.trade_result_lot = trade_result_lot
                                    trade_result.lot_table = trade_result_lot
                                trade_result.save()
                                message_types.trade_result = trade_result
                        except Exception as ex:
                            pass
                            # exit()

                        if other.text is not None:
                            other.save()
                            message_types.other = other
                        try:

                            if appoint_administration.decision_name is not None:
                                if director.name is not None:
                                    director.save()
                                    appoint_administration.director = director
                                appoint_administration.save()
                                message_types.appoint_administration = appoint_administration
                        except Exception as ex:
                            pass
                            # exit()
                        if change_administration.text is not None:
                            if director.name is not None:
                                director.save()
                                change_administration.director = director
                            change_administration.save()
                            message_types.change_administration = change_administration
                        if termination_administration.text is not None:
                            if director.name is not None:
                                director.save()
                                termination_administration.director = director
                            termination_administration.save()
                            message_types.termination_administration = termination_administration
                        if begin_executory_process.text is not None:
                            begin_executory_process.save()
                            message_types.begin_executory_process = begin_executory_process
                        if transfer_assert_for_implementation.text is not None:
                            transfer_assert_for_implementation.save()
                            message_types.transfer_assert_for_implementation = transfer_assert_for_implementation
                        if annul.text is not None:
                            annul.save()
                            message_types.annul = annul
                        if property_inventory_result.text is not None:
                            property_inventory_result.save()
                            message_types.property_inventory_result = property_inventory_result
                        if property_evaluation_report.text is not None:
                            property_evaluation_report.save()
                            message_types.property_evaluation_report = property_evaluation_report
                        if assessment_report.text is not None:
                            if appraiser.inn is not None:
                                if fio.first_name is not None:
                                    fio.save()
                                    appraiser.fio = fio
                                if sro.name is not None:
                                    sro.save()
                                    appraiser.sro = sro
                                appraiser.save()
                                appraisers.appraiser = appraiser
                                appraisers.save()
                                assessment_report.appraisers = appraisers
                            if expert_decision.number is not None or expert_decision.result is not None:
                                if expert.inn is not None:
                                    if fio.first_name is not None:
                                        fio.save()
                                        expert.fio = fio
                                    if sro.name is not None:
                                        sro.save()
                                        expert.sro = sro
                                    expert.save()
                                    experts.expert = expert
                                    experts.save()
                                    expert_decision.experts = experts
                                expert_decision.save()

                                assessment_report.expert_decision = expert_decision
                            if object_of_assessment.balance_value is not None:
                                if classifier.name is not None:
                                    classifier.save()
                                    object_of_assessment.classifier = classifier
                                object_of_assessment.save()
                                objects_of_assessments.object_of_assessment = object_of_assessment
                                assessment_report.objects_of_assessments = objects_of_assessments
                            if report.number is not None:
                                report.save()
                                assessment_report.report = report
                            assessment_report.save()
                            message_types.assessment_report = assessment_report
                        if sale_contract_result.text is not None:
                            if failure_winner_info.name is not None:
                                failure_winner_info.save()
                                sale_contract_result.failure_winner_info = failure_winner_info
                                if purchaser_info.name is not None:
                                    sale_contract_result.save()
                                    sale_contract_result.purchaser_info = purchaser_info
                            sale_contract_result.save()
                            message_types.sale_contract_result = sale_contract_result
                        if sale_contract_result2.text is not None:
                            if sale_contract_info.lot_number is not None:

                                if failure_winner_info.name is not None:
                                    failure_winner_info.save()
                                    sale_contract_info.failure_winner_info = failure_winner_info
                                sale_contract_info.save()
                                contracts.sale_contract_info = sale_contract_info
                                contracts.save()
                                sale_contract_result2.contracts = contracts
                            sale_contract_result2.save()
                            message_types.sale_contract_result2 = sale_contract_result2
                        if committee.text is not None:
                            committee.save()
                            message_types.committee = committee
                        # if committee_result.text is not None:
                        #     #other.save()
                        if sale_order_pledged_property.text is not None:
                            sale_order_pledged_property.save()
                            message_types.sale_order_pledged_property = sale_order_pledged_property
                        if receiving_creditor_demand.text is not None:
                            receiving_creditor_demand.save()
                            message_types.receiving_creditor_demand = receiving_creditor_demand
                        if  deliberate_bankruptcy.text is not None:
                            deliberate_bankruptcy.save()
                        if intention_credit_org.text is not None:
                            intention_credit_org.save()
                            message_types.intention_credit_org = intention_credit_org
                        if liabilities_credit_org.text is not None:
                            liabilities_credit_org.save()
                            message_types.liabilities_credit_org = liabilities_credit_org
                        if perfomance_credit_org.text is not None:
                            perfomance_credit_org.save()
                            message_types.perfomance_credit_org = perfomance_credit_org
                        if buying_property.text is not None:
                            buying_property.save()
                            message_types.buying_property =buying_property
                        if declaration_person_damages.text is not None:
                            if bankrupt_supervisory_person.bankrupt_supervisory_person is not None:
                                bankrupt_supervisory_person.save()
                                bankrupt_supervisory_persons.bankrupt_supervisory_person = bankrupt_supervisory_person
                                bankrupt_supervisory_person.save()
                                declaration_person_damages.bankrupt_supervisory_person = bankrupt_supervisory_person
                            if person_for_responsibility.type_person_responsibility is not None:
                                person_for_responsibility.save()
                                another_person_for_responsibility.person_for_responsibility = person_for_responsibility
                                another_person_for_responsibility.save()
                                declaration_person_damages.another_person_for_responsibility = another_person_for_responsibility
                            declaration_person_damages.save()
                            message_types.declaration_person_damages = declaration_person_damages
                        if act_person_damages.text is not None:
                            if bankrupt_supervisory_person.bankrupt_supervisory_person is not None:
                                bankrupt_supervisory_person.save()
                                bankrupt_supervisory_persons.bankrupt_supervisory_person = bankrupt_supervisory_person
                                bankrupt_supervisory_person.save()
                                act_person_damages.bankrupt_supervisory_person = bankrupt_supervisory_person
                            if person_for_responsibility.type_person_responsibility is not None:
                                person_for_responsibility.save()
                                another_person_for_responsibility.person_for_responsibility = person_for_responsibility
                                another_person_for_responsibility.save()
                                act_person_damages.another_person_for_responsibility = another_person_for_responsibility
                            act_person_damages.save()
                            message_types.act_person_damages =act_person_damages
                        if act_review_person_damages.pk is not None:
                            if bankrupt_supervisory_person.bankrupt_supervisory_person is not None:
                                bankrupt_supervisory_person.save()
                                bankrupt_supervisory_persons.bankrupt_supervisory_person = bankrupt_supervisory_person
                                bankrupt_supervisory_person.save()
                                act_review_person_damages.bankrupt_supervisory_person = bankrupt_supervisory_person
                            if person_for_responsibility.type_person_responsibility is not None:
                                person_for_responsibility.save()
                                another_person_for_responsibility.person_for_responsibility = person_for_responsibility
                                another_person_for_responsibility.save()
                                act_review_person_damages.another_person_for_responsibility = another_person_for_responsibility
                            act_review_person_damages.save()
                            message_types.act_review_person_damages =act_review_person_damages
                        if deal_invalid.text is not None:
                            if deal_participant.name is not None:
                                deal_participant.save()
                                deal_participants.deal_participant=deal_participant
                                deal_participants.save()
                                deal_invalid.deal_participants = deal_participants
                            deal_invalid.save()
                            message_types.deal_invalid = deal_invalid
                        if act_deal_invalid.text is not None:
                            if deal_participant.name is not None:
                                deal_participant.save()
                                deal_participants.deal_participant = deal_participant
                                deal_participants.save()
                                act_deal_invalid.deal_participants = deal_participants
                            act_deal_invalid.save()
                            message_types.act_deal_invalid = act_deal_invalid
                        try:
                            if act_deal_invalid2.text is not None:
                                if deal_info.deal_invalid_message_id is not None:
                                    if deal_participant.name is not None:
                                        deal_participant.save()
                                        deal_participants.deal_participant = deal_participant
                                        deal_participants.save()
                                        deal_info.deal_participants = deal_participants
                                    deal_info.save()
                                    deals.deal_info = deal_info
                                    deals.save()
                                    act_deal_invalid2.deal = deals
                                act_deal_invalid2.save()

                                message_types.act_deal_invalid2 = act_deal_invalid2
                        except Exception as ex:
                            pass
                        if act_review_deal_invalid.text is not None:
                            if deal_participant.name is not None:
                                deal_participant.save()
                                deal_participants.deal_participant = deal_participant
                                deal_participants.save()
                                act_review_deal_invalid.deal_participants = deal_participants
                            act_review_deal_invalid.save()
                            message_types.act_review_deal_invalid =act_review_deal_invalid
                        try:
                            if act_review_deal_invalid2.text is not None:
                                if act_info.act_deal_invalid_message_id is not None:
                                    if deal_info.deal_invalid_message_id is not None:
                                        if deal_participant.name is not None:
                                            deal_participant.save()
                                            deal_participants.deal_participant = deal_participant
                                            deal_participants.save()
                                            deal_info.deal_participants = deal_participants

                                        deal_info.save()
                                        deals.deal_info = deal_info
                                        deals.save()
                                        act_info.deals = deals
                                    act_info.save()
                                    acts.act_info = act_info
                                    acts.save()
                                    act_review_deal_invalid2.acts = acts
                                act_review_deal_invalid2.save()
                                message_types.act_review_deal_invalid2 =act_review_deal_invalid2
                        except Exception as ex:
                            pass
                            # exit()
                        if declaration_person_subsidiary.text is not None:
                            if bankrupt_supervisory_person.bankrupt_supervisory_person is not None:
                                bankrupt_supervisory_person.save()
                                bankrupt_supervisory_persons.bankrupt_supervisory_person = bankrupt_supervisory_person
                                bankrupt_supervisory_person.save()
                                declaration_person_subsidiary.bankrupt_supervisory_person = bankrupt_supervisory_person
                            if person_for_responsibility.type_person_responsibility is not None:
                                person_for_responsibility.save()
                                another_person_for_responsibility.person_for_responsibility = person_for_responsibility
                                another_person_for_responsibility.save()
                                declaration_person_subsidiary.another_person_for_responsibility = another_person_for_responsibility
                            declaration_person_subsidiary.save()
                            message_types.declaration_person_subsidiary = declaration_person_subsidiary
                        if act_person_subsidiary.text is not None:
                            if bankrupt_supervisory_person.bankrupt_supervisory_person is not None:
                                bankrupt_supervisory_person.save()
                                bankrupt_supervisory_persons.bankrupt_supervisory_person = bankrupt_supervisory_person
                                bankrupt_supervisory_person.save()
                                act_person_subsidiary.bankrupt_supervisory_person = bankrupt_supervisory_person
                            act_person_subsidiary.save()
                            message_types.act_person_subsidiary =act_person_subsidiary
                        try:
                            if act_person_subsidiary2.text is not None:
                                if message.number is not None:
                                    if bankrupt_supervisory_person.name is not None:
                                        bankrupt_supervisory_person.save()
                                        bankrupt_supervisory_persons.bankrupt_supervisory_person = bankrupt_supervisory_person
                                        bankrupt_supervisory_persons.save()
                                        message.bankrupt_supervisory_persons = bankrupt_supervisory_persons
                                    message.save()
                                    declaration_person_subsidiary_info_messages.message = message
                                    declaration_person_subsidiary_info_messages.save()
                                    act_person_subsidiary2.declaration_person_subsidiary_info_message = declaration_person_subsidiary_info_messages

                                act_person_subsidiary2.save()
                                message_types.act_person_subsidiary2 =act_person_subsidiary2
                        except Exception as ex:
                            pass
                            # exit()
                        if act_review_person_subsidiary.text is not None:
                            if bankrupt_supervisory_person.name is not None:
                                bankrupt_supervisory_person.save()
                                bankrupt_supervisory_persons.bankrupt_supervisory_person = bankrupt_supervisory_person
                                bankrupt_supervisory_persons.save()
                                act_review_person_subsidiary.bankrupt_supervisory_persons = bankrupt_supervisory_persons
                            act_review_person_subsidiary.save()
                            message_types.act_review_person_subsidiary = act_review_person_subsidiary
                        try:
                            if act_review_person_subsidiary2.text is not None:
                                if bankrupt_supervisory_person.name is not None:
                                    bankrupt_supervisory_person.save()
                                    bankrupt_supervisory_persons.bankrupt_supervisory_person = bankrupt_supervisory_person
                                    bankrupt_supervisory_persons.save()
                                    message.bankrupt_supervisory_persons = bankrupt_supervisory_persons
                                message.save()
                                act_person_subsidiary_info_messages.message = message
                                act_person_subsidiary_info_messages.save()
                                act_review_person_subsidiary2.act_person_subsidiary_info_messages = act_person_subsidiary_info_messages
                                act_review_person_subsidiary2.save()
                                message_types.act_review_person_subsidiary2 = act_review_person_subsidiary2
                        except Exception as ex:
                            pass
                            # exit()
                        if meeting_worker.text is not None:
                            meeting_worker.save()
                            message_types.meeting_worker = meeting_worker
                        if meeting_worker_result.text is not None:
                            meeting_worker_result.save()
                            message_types.meeting_worker_result = meeting_worker_result
                        if view_draft_restructuring_plan.text is not None:
                            view_draft_restructuring_plan.save()
                            message_types.view_draft_restructuring_plan = view_draft_restructuring_plan
                        if view_exec_restructuring_plan.text is not None:
                            view_exec_restructuring_plan.save()
                            message_types.view_exec_restructuring_plan =view_exec_restructuring_plan
                        try:
                            if transfer_ownership_real_estate.text is not None:
                                if land_plot.cadastral_number is not None or land_plot.ownership_right_description is not None:
                                    land_plot.save()
                                    land_plots.land_plot = land_plot
                                    land_plots.save()
                                    transfer_ownership_real_estate.land_plots = land_plots
                                if uncompleted_building_project.cadastral_number is not None or uncompleted_building_project.address is not None :
                                    uncompleted_building_project.save()
                                    uncompleted_building_projects.uncompleted_building_project = uncompleted_building_project
                                    uncompleted_building_projects.save()
                                    transfer_ownership_real_estate.uncompleted_building_projects = uncompleted_building_projects
                                transfer_ownership_real_estate.save()
                                message_types.transfer_ownership_real_estate =transfer_ownership_real_estate
                        except Exception as ex:
                            pass
                            # exit()
                        if cancel_auction_trade_result.text is not None:
                            cancel_auction_trade_result.save()
                            message_types.cancel_auction_trade_result = cancel_auction_trade_result
                        if cancel_deliberate_bankruptcy.text is not None:
                            cancel_deliberate_bankruptcy.save()
                            message_types.cancel_deliberate_bankruptcy = cancel_deliberate_bankruptcy
                        if change_auction.id_changed_message is not None or change_auction.text is not None:
                            change_auction.save()
                        if change_deliberate_bankruptcy.text is not None:
                            change_deliberate_bankruptcy.save()
                            message_types.change_deliberate_bankruptcy = change_deliberate_bankruptcy
                        if reducing_size_share_capital.text is not None:
                            reducing_size_share_capital.save()
                            message_types.reducing_size_share_capital = reducing_size_share_capital
                        if selection_purchaser_assets.text is not None:
                            selection_purchaser_assets.save()
                        if estimates_current_expenses.text is not None:
                            estimates_current_expenses.save()
                            message_types.estimates_current_expenses = estimates_current_expenses
                        if order_and_timing_calculations.text is not None:
                            order_and_timing_calculations.save()
                            message_types.order_and_timing_calculations = order_and_timing_calculations
                        if information_about_bankruptcy.text is not None:
                            information_about_bankruptcy.save()
                            message_types.information_about_bankruptcy =information_about_bankruptcy
                        if estimates_and_unsold_assets.text is not None:
                            estimates_and_unsold_assets.save()
                            message_types.estimates_and_unsold_assets =estimates_and_unsold_assets
                        if remaining_assets_and_right.text is not None:
                            remaining_assets_and_right.save()
                            message_types.remaining_assets_and_right =remaining_assets_and_right
                        if impending_transfer_assets.text is not None:
                            if credit_organization_info.name is not None or  credit_organization_info.address is not None:
                                credit_organization_info.save()
                                credit_organizations.credit_organization_info = credit_organization_info
                                credit_organizations.save()
                                impending_transfer_assets.credit_organizations =credit_organizations
                            impending_transfer_assets.save()
                            message_types.impending_transfer_assets =impending_transfer_assets
                        if transfer_assets.text is not None:
                            transfer_assets.save()
                            message_types.transfer_assets =transfer_assets
                        if transfer_insurance_portfolio.text is not None:
                            if insurance_organization.name is not None or insurance_organization.address is not None:
                                insurance_organization.save()
                                transfer_insurance_portfolio.insurance_organization = insurance_organization
                            transfer_insurance_portfolio.save()
                            message_types.transfer_insurance_portfolio = transfer_insurance_portfolio
                        if bank_open_account_debtor.text is not None:
                            bank_open_account_debtor.save()
                            message_types.bank_open_account_debtor =bank_open_account_debtor
                        if procedure_granting_indemnity.text is not None:
                            procedure_granting_indemnity.save()
                            message_types.procedure_granting_indemnity = procedure_granting_indemnity
                        if right_unsold_asset.text is not None:
                            right_unsold_asset.save()
                            message_types.right_unsold_asset =right_unsold_asset
                        if transfer_responsibilities_fund.text is not None:
                            transfer_responsibilities_fund.save()
                            message_types.transfer_responsibilities_fund = transfer_responsibilities_fund
                        if extension_administration.text is not None:
                            extension_administration.save()
                            message_types.extension_administration = extension_administration
                        if meeting_participants_building.text is not None:
                            meeting_participants_building.save()
                            message_types.meeting_participants_building = meeting_participants_building
                        if meeting_part_build_result.text is not None:
                            meeting_part_build_result.save()
                            message_types.meeting_part_build_result = meeting_part_build_result
                        if part_build_monetary_claim.text is not None:
                            part_build_monetary_claim.save()
                            message_types.part_build_monetary_claim =part_build_monetary_claim
                        if start_settlement.text is not None:
                            start_settlement.save()
                            message_types.start_settlement =start_settlement
                        if process_inventory_debtor.text is not None:
                            process_inventory_debtor.save()
                            message_types.process_inventory_debtor =process_inventory_debtor
                        if rebuttal.text is not None:
                            rebuttal.save()
                            message_types.rebuttal =rebuttal
                        if creditor_choice_right_subsidiary.text is not None:
                            creditor_choice_right_subsidiary.save()
                            message_types.creditor_choice_right_subsidiary = creditor_choice_right_subsidiary
                        if accession_declaration_subsidiary.text is not None:
                            accession_declaration_subsidiary.save()
                            message_types.accession_declaration_subsidiary = accession_declaration_subsidiary
                        if disqualification_arbitration_manager.text is not None:
                            if arbitr_manager.snils is not None or arbitr_manager.fio is not None:
                                arbitr_manager.save()
                                disqualification_arbitration_manager.arbitr_manager = arbitr_manager
                            if court.name is not None or court.code is not None:
                                court.save()
                                disqualification_arbitration_manager.court = court
                            disqualification_arbitration_manager.save()
                            message_types.disqualification_arbitration_manager =disqualification_arbitration_manager
                        if disqualification_arbitration_manager2.text is not None:
                            if arbitr_manager.snils is not None or arbitr_manager.fio is not None:
                                arbitr_manager.save()
                                disqualification_arbitration_manager2.arbitr_manager = arbitr_manager
                            if court.name is not None or court.code is not None:
                                court.save()
                                disqualification_arbitration_manager2.court = court
                            if duration.day is not None or duration.month is not None or duration.year is not None:
                                duration.save()
                                disqualification_arbitration_manager2.duration = duration
                            disqualification_arbitration_manager2.save()
                            message_types.disqualification_arbitration_manager2 = disqualification_arbitration_manager2
                        if change_estimates_current_expenses.text is not None:
                            change_estimates_current_expenses.save()
                            message_types.change_estimates_current_expenses =change_estimates_current_expenses
                        if return_of_application_on_extrajudicial_bankruptcy.date is not None or return_of_application_on_extrajudicial_bankruptcy.no_return_of_enforcement_documen is not None:
                            return_of_application_on_extrajudicial_bankruptcy.save()
                            message_types.return_of_application_on_extrajudicial_bankruptcy = return_of_application_on_extrajudicial_bankruptcy
                        if start_of_extrajudicial_bankruptcy.pk is not None:
                            if bank.name is not None or bank.bank_identifier is not None:
                                bank.save()
                                banks.bank = bank
                                banks.save()
                                start_of_extrajudicial_bankruptcy.banks = banks
                            if creditors_non_from_entrepreneurship.non_monetary_obligations is not None:
                                if monetary_obligation.creditor_name is not None or monetary_obligation.creditor_region is not None:
                                    monetary_obligation.save()
                                    monetary_obligations.monetary_obligation = monetary_obligation
                                    monetary_obligations.save()
                                    creditors_non_from_entrepreneurship.monetary_obligations = monetary_obligations
                                if obligatory_payment.name is not None:
                                    obligatory_payment.save()
                                    obligatory_payments.obligatory_payment = obligatory_payment
                                    obligatory_payments.save()
                                    creditors_non_from_entrepreneurship.obligatory_payments = obligatory_payments
                                creditors_non_from_entrepreneurship.save()
                                start_of_extrajudicial_bankruptcy.creditors_non_from_entrepreneurship = creditors_non_from_entrepreneurship
                            if creditors_from_entrepreneurship.non_monetary_obligations is not None:
                                if monetary_obligation.creditor_name is not None or monetary_obligation.creditor_region is not None:
                                    monetary_obligation.save()
                                    monetary_obligations.monetary_obligation = monetary_obligation
                                    monetary_obligations.save()
                                    creditors_from_entrepreneurship.monetary_obligations = monetary_obligations
                                if obligatory_payment.name is not None:
                                    obligatory_payment.save()
                                    obligatory_payments.obligatory_payment = obligatory_payment
                                    obligatory_payments.save()
                                    creditors_from_entrepreneurship.obligatory_payments = obligatory_payments
                                creditors_from_entrepreneurship.save()
                                start_of_extrajudicial_bankruptcy.creditors_from_entrepreneurship = creditors_from_entrepreneurship
                            start_of_extrajudicial_bankruptcy.save()
                            message_types.start_of_extrajudicial_bankruptcy =start_of_extrajudicial_bankruptcy
                        if termination_of_extrajudicial_bankruptcy.pk is not None:
                            termination_of_extrajudicial_bankruptcy.save()
                            message_types.termination_of_extrajudicial_bankruptcy = termination_of_extrajudicial_bankruptcy
                        if completion_of_extrajudicial_bankruptcy.pk is not None:
                            completion_of_extrajudicial_bankruptcy.save()
                            message_types.completion_of_extrajudicial_bankruptcy = completion_of_extrajudicial_bankruptcy
                        message_types.save()
                        message_info.message_types = message_types
                        message_info.save()
                except Exception as ex:
                    pass
                    #print("$"*50)
                    # pass
                try:
                    if message_data.id_message_data is not None:
                        message_data.publisher = publisher
                        message_data.message_info = message_info

                        message_data.save()
                except Exception as ex:
                    pass
            except Exception as ex:
                pass
    except Exception as ex:
        pass
