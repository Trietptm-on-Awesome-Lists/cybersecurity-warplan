"""
A website domain like "discuss.leetcode.com" consists of various subdomains.
At the top level, we have "com", at the next level, we have "leetcode.com",
and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com",
we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received),
followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains,
 (in the same format as the input, and in any order),
  that explicitly counts the number of visits to each subdomain.

Example 1:
Input:
["9001 discuss.leetcode.com"]
Output:
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation:
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

Example 2:
Input:
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output:
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation:
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

Notes:

    The length of cpdomains will not exceed 100.
    The length of each domain name will not exceed 100.
    Each address will have either 1 or 2 "." characters.
    The input count in any count-paired domain will not exceed 10000.
    The answer output can be returned in any order.
"""
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domainz = {}
        for c in cpdomains:
            count, domains = c.split(' ')
            domainz[domains] = domainz.get(domains, 0) + int(count)
            while len(domains.split('.')) != 1:
                domains = domains.split('.',1)[1]
                domainz[domains] = domainz.get(domains, 0) + int(count)

        res = [str(domainz[x]) + ' ' + str(x) for x in domainz]
        return (res)
sol = Solution()

cp = ["2913 ret.ych.ca","9172 zfz.net","2979 bhp.org","5016 gqi.co","2406 ocf.co","7344 czb.com","3314 ytd.hkt.net","3624 vmv.epf.network","8342 srp.team","2444 gxz.team","2444 vks.gxz.team","9374 jep.ato.co","767 epf.us","58413 com","3528 jyx.arz.us","9897 lra.uyy.org","4198 okv.co","5705 mqa.wsv.net","408 zfz.network","5705 wsv.net","3496 ytn.com","4806 dfa.co","4521 weh.bfo.us","7464 fff.co","12367 bfo.team","6122 nqk.srp.org","1523 bhp.co","817 sgp.htq.co","7476 yvr.net","3449 tfm.us","2471 czb.us","8557 uai.lfn.net","7193 fzx.ca","7042 btv.com","84 lmm.network","1110 znq.us","3609 bhp.team","3875 ato.network","3111 gdw.team","81314 network","1137 ujs.qzi.co","9374 ato.co","1627 bhp.ca","8167 jre.team","3855 yjt.network","3528 arz.us","622 cwn.net","4126 lir.ajl.team","2160 hsj.epf.org","8544 bhp.com","3950 xuf.network","8928 arz.org","51516 us","2777 nak.mkw.co","8176 ujm.gqs.ca","1789 xcf.zqy.ca","1387 gbq.org","3262 ixi.us","2777 mkw.co","9103 vbo.org","2715 ubt.okv.us","654 yls.yjt.co","6129 hkt.com","6920 dfa.us","3875 brk.ato.network","2406 hkb.ocf.co","4521 bfo.us","32 ulz.com","2740 xhe.org","1873 kse.gjf.ca","9846 fuw.org","2531 ser.com","7292 ksc.net","9372 hci.jia.network","6865 thk.net","2715 okv.us","4602 weq.buf.team","3090 yjt.us","4439 gtu.us","4126 ajl.team","7464 jpd.fff.co","7292 zbl.ksc.net","654 yjt.co","9531 hoh.co","622 wmt.cwn.net","9530 omu.network","5041 hwu.us","4296 xtb.jre.us","2329 vva.qay.network","3055 fdy.jkx.com","3215 hoh.network","8176 gqs.ca","817 htq.co","59758 co","5041 cdf.hwu.us","1781 lbk.ksc.co","36170 ca","4681 ytn.network","3322 xhe.team","8544 xrj.bhp.com","5016 zwv.gqi.co","5907 zfz.us","8167 ahm.jre.team","1387 hju.gbq.org","3262 mor.ixi.us","8557 lfn.net","5729 srp.com","6920 tlc.dfa.us","8263 cwn.org","6122 srp.org","2572 qay.network","7968 gjf.network","2913 ych.ca","7392 uyy.net","2447 ksc.com","64390 org","2965 gxj.org","4806 xss.dfa.co","9259 bfo.net","654 yaw.lmm.ca","6629 vdu.bfo.team","1110 kdd.znq.us","9523 cgl.network","1501 ara.ca","1789 zqy.ca","3624 epf.network","4296 jre.us","68516 net","3090 ycc.yjt.us","8274 ulz.co","7476 cze.yvr.net","4198 xfs.okv.co","4681 lwf.ytn.network","9372 jia.network","1781 ksc.co","3215 bll.hoh.network","3055 jkx.com","6890 bfo.network","1137 qzi.co","9897 uyy.org","8390 zqk.network","408 tdt.zfz.network","1225 lmm.ca","4602 buf.team","4975 okv.com","2862 sci.net","2160 epf.org","2531 mce.ser.com","7193 xth.fzx.ca","3314 hkt.net","2862 coh.sci.net","9523 wyv.cgl.network","5738 lar.bfo.team","1523 suq.bhp.co","7089 ske.yls.com","7089 yls.com","9581 gqi.team","3377 jkx.network","9219 tfm.ca","1873 gjf.ca","767 irh.epf.us","59671 team"]

sol.subdomainVisits(cp)

"""
["408 zfz.network","1789 zqy.ca","622 cwn.net","6629 vdu.bfo.team","817 htq.co","3496 ytn.com","6122 nqk.srp.org","4296 jre.us","8176 gqs.ca","7292 zbl.ksc.net","4126 lir.ajl.team","84 lmm.network","622 wmt.cwn.net","2572 qay.network","7089 ske.yls.com","2979 bhp.org","2740 xhe.org","4439 gtu.us","1110 kdd.znq.us","3314 hkt.net","5041 cdf.hwu.us","4198 okv.co","6920 tlc.dfa.us","654 yjt.co","5016 zwv.gqi.co","59671 team","5705 mqa.wsv.net","9103 vbo.org","2406 hkb.ocf.co","7292 ksc.net","8928 arz.org","8342 srp.team","2447 ksc.com","32 ulz.com","3855 yjt.network","9530 omu.network","2329 vva.qay.network","2531 ser.com","1781 lbk.ksc.co","7476 cze.yvr.net","1873 gjf.ca","3950 xuf.network","1789 xcf.zqy.ca","3055 jkx.com","81314 network","1137 qzi.co","3262 mor.ixi.us","7344 czb.com","3090 yjt.us","6890 bfo.network","3875 ato.network","68516 net","9374 jep.ato.co","9523 cgl.network","7464 jpd.fff.co","2715 okv.us","3528 arz.us","9374 ato.co","7042 btv.com","64390 org","2862 sci.net","9259 bfo.net","9172 zfz.net","3055 fdy.jkx.com","2160 hsj.epf.org","5907 zfz.us","7392 uyy.net","9897 lra.uyy.org","58413 com","2406 ocf.co","6129 hkt.com","3377 jkx.network","12367 bfo.team","59758 co","36170 ca","2160 epf.org","4602 weq.buf.team","6920 dfa.us","1879 lmm.ca","3314 ytd.hkt.net","2862 coh.sci.net","2913 ret.ych.ca","817 sgp.htq.co","9531 hoh.co","3609 bhp.team","8274 ulz.co","9846 fuw.org","1501 ara.ca","2913 ych.ca","5738 lar.bfo.team","8557 lfn.net","3449 tfm.us","654 yls.yjt.co","1781 ksc.co","3215 hoh.network","2777 mkw.co","9897 uyy.org","767 irh.epf.us","2444 gxz.team","4806 xss.dfa.co","9372 hci.jia.network","9581 gqi.team","5016 gqi.co","4975 okv.com","4296 xtb.jre.us","5705 wsv.net","9372 jia.network","8544 bhp.com","1873 kse.gjf.ca","7464 fff.co","3624 epf.network","9219 tfm.ca","1387 hju.gbq.org","4806 dfa.co","3262 ixi.us","7193 fzx.ca","2965 gxj.org","8557 uai.lfn.net","51516 us","8176 ujm.gqs.ca","4602 buf.team","4126 ajl.team","1110 znq.us","2444 vks.gxz.team","6865 thk.net","1523 suq.bhp.co","3111 gdw.team","4521 weh.bfo.us","7476 yvr.net","8167 jre.team","5041 hwu.us","4521 bfo.us","3322 xhe.team","2777 nak.mkw.co","8263 cwn.org","4681 lwf.ytn.network","654 yaw.lmm.ca","8167 ahm.jre.team","3215 bll.hoh.network","4681 ytn.network","767 epf.us","6122 srp.org","3528 jyx.arz.us","408 tdt.zfz.network","8390 zqk.network","9523 wyv.cgl.network","3624 vmv.epf.network","3090 ycc.yjt.us","8544 xrj.bhp.com","1523 bhp.co","4198 xfs.okv.co","7968 gjf.network","3875 brk.ato.network","1387 gbq.org","2471 czb.us","1627 bhp.ca","1137 ujs.qzi.co","5729 srp.com","7089 yls.com","7193 xth.fzx.ca","2715 ubt.okv.us","2531 mce.ser.com"]

['2777 nak.mkw.co', '2777 mkw.co', '59758 co', '654 yaw.lmm.ca', '1225 lmm.ca', '36170 ca', '3528 jyx.arz.us', '3528 arz.us', '51516 us', '3215 bll.hoh.network', '3215 hoh.network', '81314 network', '408 tdt.zfz.network', '408 zfz.network', '3322 xhe.team', '59671 team', '8342 srp.team', '9259 bfo.net', '68516 net', '3875 brk.ato.network', '3875 ato.network', '2531 mce.ser.com', '2531 ser.com', '58413 com', '2471 czb.us', '4806 xss.dfa.co', '4806 dfa.co', '654 yls.yjt.co', '654 yjt.co', '767 irh.epf.us', '767 epf.us', '1501 ara.ca', '2572 qay.network', '9103 vbo.org', '64390 org', '6890 bfo.network', '4296 xtb.jre.us', '4296 jre.us', '2329 vva.qay.network', '9846 fuw.org', '4681 lwf.ytn.network', '4681 ytn.network', '1781 lbk.ksc.co', '1781 ksc.co', '7464 jpd.fff.co', '7464 fff.co', '2740 xhe.org', '4602 weq.buf.team', '4602 buf.team', '3055 fdy.jkx.com', '3055 jkx.com', '5705 mqa.wsv.net', '5705 wsv.net', '6629 vdu.bfo.team', '12367 bfo.team', '9897 lra.uyy.org', '9897 uyy.org', '8167 ahm.jre.team', '8167 jre.team', '9374 jep.ato.co', '9374 ato.co', '3624 vmv.epf.network', '3624 epf.network', '6865 thk.net', '6920 tlc.dfa.us', '6920 dfa.us', '9372 hci.jia.network', '9372 jia.network', '7968 gjf.network', '7292 zbl.ksc.net', '7292 ksc.net', '2862 coh.sci.net', '2862 sci.net', '3855 yjt.network', '1387 hju.gbq.org', '1387 gbq.org', '817 sgp.htq.co', '817 htq.co', '2406 hkb.ocf.co', '2406 ocf.co', '622 wmt.cwn.net', '622 cwn.net', '9172 zfz.net', '1523 suq.bhp.co', '1523 bhp.co', '9581 gqi.team', '2160 hsj.epf.org', '2160 epf.org', '32 ulz.com', '1137 ujs.qzi.co', '1137 qzi.co', '5041 cdf.hwu.us', '5041 hwu.us', '4126 lir.ajl.team', '4126 ajl.team', '3111 gdw.team', '8928 arz.org', '9531 hoh.co', '7344 czb.com', '2715 ubt.okv.us', '2715 okv.us', '1110 kdd.znq.us', '1110 znq.us', '5729 srp.com', '6122 nqk.srp.org', '6122 srp.org', '7193 xth.fzx.ca', '7193 fzx.ca', '3496 ytn.com', '3950 xuf.network', '4521 weh.bfo.us', '4521 bfo.us', '3262 mor.ixi.us', '3262 ixi.us', '4975 okv.com', '7089 ske.yls.com', '7089 yls.com', '4198 xfs.okv.co', '4198 okv.co', '2444 vks.gxz.team', '2444 gxz.team', '1789 xcf.zqy.ca', '1789 zqy.ca', '7392 uyy.net', '3449 tfm.us', '5907 zfz.us', '9530 omu.network', '3314 ytd.hkt.net', '3314 hkt.net', '9523 wyv.cgl.network', '9523 cgl.network', '4439 gtu.us', '8390 zqk.network', '1627 bhp.ca', '3609 bhp.team', '8557 uai.lfn.net', '8557 lfn.net', '2913 ret.ych.ca', '2913 ych.ca', '2447 ksc.com', '7476 cze.yvr.net', '7476 yvr.net', '8544 xrj.bhp.com', '8544 bhp.com', '6129 hkt.com', '8274 ulz.co', '9219 tfm.ca', '5016 zwv.gqi.co', '5016 gqi.co', '5738 lar.bfo.team', '3377 jkx.network', '2979 bhp.org', '8176 ujm.gqs.ca', '8176 gqs.ca', '84 lmm.network', '3090 ycc.yjt.us', '3090 yjt.us', '7042 btv.com', '2965 gxj.org', '8263 cwn.org', '1873 kse.gjf.ca', '1873 gjf.ca']
"""