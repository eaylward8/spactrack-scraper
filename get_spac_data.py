import csv
import requests


URL = 'https://api.spactrack.net/spacs/query/1,5/options,commonSymbol,initialCommonSymbol,commonSymbolTickerName,companyName,targetCompany,spacStatuswithUnitSplitStatus,targetFocus,targetCompanyPrint,targetCompanyWithDADate,leadership,trustValue,marketCap,unitWarrantDetails,commonLatestPrice,commonChangePercent,commonReturnFromIPOShareAdjusted,ipoPrice,commonExtendedPrice,commonExtendedChangePercent,commonOutstandingShares,commonPreviousDayVolume,commonVolumePercentChangePreviousDay,commonWeekPercentChange,commonMonthPercentChange,commonWeek52High,commonWeek52Low,unitLatestPrice,unitChangePercent,commonLatestVolume,warrantLatestPrice,warrantChangePercent,splitDate,estimatedSplitDate,warrantIntrinsicValue,unitExtendedPrice,unitExtendedChangePercent,unitLatestVolume,unitPreviousDayVolume,unitVolumePercentChangePreviousDay,unitWeekPercentChange,unitMonthPercentChange,unitWeek52High,unitWeek52Low,ipoDate,combinedFocus,finalSector,warrantExtendedPrice,ipoSize,underWriters,estimatedCompletionDate,approvedExtDate,percentProgressToDeadline,upcExtVoteLink,extensionNotesDV,SECFilingDatabaseLink,filingLink,spacFinalS1Link,definitiveAgreementDate,timeBetweenIPOAndDA,definitiveAgreementLink,investorPresentationLink,sizePIPEandFPA,optionable,warrantExtendedChangePercent,warrantLatestVolume,warrantVolumePercentChangePreviousDay,warrantWeekPercentChange,warrantMonthPercentChange,warrantWeek52High,warrantWeek52Low,proFormaEquityValue,proFormaEV,mergerVoteDate,mergerVoteLink,redemptionDeadlineDate,postMergeImpliedProFormaMarketCapCurrentCommonPrice,warrantSymbol,unitSymbol,completedSymbolPrint,lawyers,trustValuePerShareNAVPS,updatedInvestorPresentation,filingDate,country,city,sponsorName,sponsorAffiliate,sponsorManager,exchange,proFormaTotalShares,proFormaMarketCapCurrentCommon,proFormaEVCurrentCommon,projectedRevenue2022,estimatedValue2022Projection,projectedRevenue2024,estimatedValue2024Projection,recentIPO,newRegistration,wellKnownSponsor,serialSponsor,inTalksReport,inTalksLink,dealFellThrough,topTierUnderWriter,totalSharesPIPE,activeStatus,hasRights,postSPACSymbol,postSPACName,postSPACCompletionEvents,warrantTradingStatus,mover,postSPACClosingPressRelease,estimatedWarrantExerciseDate,deSPACestimatedDateWarrantsExercisable,deSPACwarrantExerciseDeadline,priceOnMergeDate,percentMoveSinceMerge,commonTradingStatus,commonBelow10,warrantBelow1,unitBelow10,trustSizeCategory,hasRights,recentSplit,isRecentDefinitiveAgreement,isRecentIPO,deadlineWithinTwoMonths,deadlineWithinOneMonth,deadlineWithinThreeMonths,deadlineWithinFourMonths,status,isInTalksUnconfirmed,isActiveSPAC,isLiquidatingOrEarlyLiquidation,industryTagsMP,themesMP,otherTagsMP,isPendingS1Effective,cashTagSymbol,initialCommonSymbol,statusDetails'

# If the script fails and the message provided is something like "Unauthorized" or "Log in again", follow these steps:
#
# 1. Go to https://spactrack.io/spacs/ in your browser
# 2.
HEADERS = {
  'Authorization': 'Bearer ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmhZMk5sYzNNaU9uc2lhWFJsY21GMGFXOXVJam9pYzNWaWMyVnhkV1Z1ZENJc0luTmxZM0psZENJNklsNXdRV28wVGtKWlpWWlJRWEl5U0NaMU1uRnROeW9tUkU1MFhpUmxKVFI0YVdGbWFWb2taV3BFVkZkQmFVMWlkR3h6SW4wc0luTmpiM0JsY3lJNld5SjNZWFJqYUd4cGMzUXZiRzloWkNJc0luZGhkR05vYkdsemRDOTFjR1JoZEdVaUxDSnpjR0ZqY3k5eGRXVnllU0lzSW5Od1lXTnpMMkZrZG1GdVkyVmtVWFZsY25raUxDSnpjR0ZqY3k5elpXRnlZMmdpTENKemNHRmpjeTlrWlhSaGFXd2lMQ0oxYzJWeUwzSmxabkpsYzJoVWIydGxiaUpkTENKcFlYUWlPakUyTnpZNE5EQTJOVElzSW1WNGNDSTZNVFkzTmpreU56QTFNaXdpWVhWa0lqcGJJa0ZWUkVsRlRrTkZYMVZUUlZJaVhTd2lhWE56SWpvaVJrbE9WRkpCUTBzaUxDSnpkV0lpT2lKMWMyVnlRR052YlcxdmJtWnBMbU52YlNKOS5aVGY2WU5nRjVra0Y2bDg3eGtOTDVYU3lDSnVsTEZMR0JON1JITk1LaG5V'
}

def get_spac_data():
  res = requests.get(URL, headers=HEADERS)

  if res.status_code != 200:
    print('Error! Request unsuccessful.')
    print(f'Status code: {res.status_code}')
    print(f'Text: {res.text}')
    return
  else:
    json = res.json()
    spacs = json['data']
    headers = spacs[0].keys()
    headers = [
      'commonSybmol',
      'initialCommonSymbol',
      'companyName',
      'spacStatuswithUnitSplitStatus',
      'targetCompany',
      'targetFocus',
      'targetCompanyWithDADate',
      'leadership',
      'trustValue',
      'marketCap',
      'unitWarrantDetails',
      'commonLatestPrice',
      'commonChangePercent',
      'unitLatestPrice',
      'unitChangePercent',
      'warrantLatestPrice',
      'warrantChangePercent',
      'splitDate',
      'warrantIntrinsicValue',
      'ipoDate',
      'ipoSize',
      'underWriters',
      'estimatedCompletionDate',
      'percentProgressToDeadline',
      'SECFilingDatabaseLink',
      'spacFinalS1Link'
    ]

    for spac in spacs:
      for key in spac.keys():
        if key not in headers:
          headers.append(key)

    with open('spac_data.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)

        # write the headers to the CSV file
        writer.writeheader()

        # write each dictionary to the CSV file
        for spac in spacs:
            writer.writerow(spac)


get_spac_data()