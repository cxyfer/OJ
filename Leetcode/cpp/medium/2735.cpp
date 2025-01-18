/*
 * @lc app=leetcode id=2735 lang=cpp
 * @lcpr version=30112
 *
 * [2735] Collecting Chocolates
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
class Solution {
public:
    long long minCost(vector<int>& nums, int x) {
        LL n = nums.size();
        vector<LL> ans(n, 0); // ans[k] 表示操作k次時，收集所有種類巧克力的最小總花費
        for (int i=1; i<n; ++i) {
            ans[i] = (LL) x * i;
        }
        for (int i=0; i<n; ++i) {
            int cost = nums[i];
            for (int k=0; k<n; ++k) { // 第i種巧克力，操作 k 次時的最小花費
                cost = min(cost, nums[(i+k)%n]);
                ans[k] += (LL) cost;
            }
        }
        LL res = ans[0];
        for (int i=1; i<n; ++i) {
            res = min(res, ans[i]);
        }
        return res;
    }
};
// @lc code=end
int main() {
    Solution sol = Solution();
    vector<int> nums1 = {20,1,15};
    cout << sol.minCost(nums1, 5) << endl;
    vector<int> nums2 = {299233249,115957782,228604572,448861527,301894606,21222461,240516522,358246868,413976961,415202034,347145694,25179641,67012757,23179028,298860892,393980568,96107833,440107016,368062496,431711950,168495823,288886371,264379963,131340167,123383433,210330983,169702261,231198087,347233240,244334342,231146993,417698327,276674107,429592140,276529898,441002180,118671082,424882382,388447105,283394854,22633834,74753172,120470124,323441806,38843323,396656876,146719905,81381072,20928831,142011150,375347929,383655529,334637218,89892827,10388535,337727937,286008702,70033655,63851701,199791215,133096408,459169699,93654569,252074970,198614520,37253714,340718318,50490837,111264032,204293506,166444070,101236904,340263246,107052157,121920540,79285822,252482375,155000421,312461468,291953784,249545540,267081591,386107411,458018816,131256995,243856205,388962233,159927496,431333783,300956254,265114032,437936127,160957077,204946646,409443985,390319463,115802639,151810502,75695172,81269944,93748440,435038660,167634366,250727359,466131817,135596265,407620679,11050683,303434576,2236598,47230416,367765453,358526852,123049603,402383960,298937400,179867941,464980808,182111431,25168531,117630653,374998153,25980770,68956656,418772492,465511058,207991509,234443697,14073545,39807284,116279483,178692521,102249503,10046776,265075815,32008749,182808214,424797502,376239486,441721343,425748571,92799045,422218030,176049724,103922605,208890821,27414157,291905056,383788462,382686682,98356276,42252848,128059568,392100727,90183367,244300236,117268958,90320568,141180462,466797209,331580726,237197610,402033877,87767490,11821606,30875693,193811073,411331376,33325206,200680472,72285432,281037820,352190749,167148649,295225312,402730202,151336849,77623715,216983093,115763929,144859473,65127217,467014077,332552283,183253042,256584094,150843809,253890216,57179821,131111795,227619806,3614266,246243251,382484722,418598116,121293042,44837355,192270542,222182323,288993804,254783942,293943076,62763721,360695094,217962469,233994774,198993096,342053540,162262355,469186487,241600657,390982215,32947608,426152604,296401828,426434968,294124173,115470480,316737431,259190285,470294959,383883678,89852425,25477297,391297663,411697374,342815233,111688702,162778253,190130468,404431207,236208495,27068534,311477721,299441918,433001504,216969758,92977065,458070284,383226871,390873710,294235361,139295390,175229138,29909693,176808099,272013489,5673120,105012895,182206445,422767068,357981151,46784456,391760581,4383416,219243938,82256102,324834710,346357317,470381239,421391345,299076551,190816562,143683066,148885270,409150845,315386300,152127626,114567353,403220611,161640119,304226979,17665108,278831728,164531037,181408918,60476620,258850156,119443593,336766229,392390035,90181851,113800547,325550919,325469394,16376925,80586828,380215440,63179688,310336746,13872434,22284664,76071079,50466364,110772140,194131862,72632293,111267225,379073755,424538565,384768496,362069665,336533830,7996733,384169172,277064028,226116627,258990838,33006563,154291040,408495133,407215110,136537884,91646462,27881038,370927223,356546147,398705699,401408585,230242109,235791983,149792102,368144555,284135631,78257233,249678882,83904516,254941797,393781585,142325678,77955401,215073549,282695550,472632001,334783185,434135655,167299655,257091217,109382651,237667814,397790035,410031522,275958411,213764599,243329168,431928664,323017110,138283570,397332242,465334345,344035609,341356101,341558418,261991828,135590969,402050381,3498831,276650442,379471029,103514642,245420870,26086918,266930270,191781390,282939354,53909211,328637117,353617748,274759823,121283156,220449390,466706113,366480997,293355845,410602954,8612130,422355329,191437000,13340585,386347163,281728332,232874916,318791960,42451727,169065520,453077651,21677400,322506484,295578085,135521464,257130667,411651808,286974459,300209229,435050418,300755329,234803698,27375305,363646177,351010847,15726919,141727964,205452959,149936698,146131880,21625712,391097592,106647337,134498501,422834751,468153148,309933625,455262970,109495986,168989056,126526030,196904017,164975113,216857487,1115389,60798213,100272564,80441715,180630312,187754942,24620666,369943933,260987399,144143361,148236435,444139167,230490439,158223383,315983955,344449899,171176079,333055623,1119800,458392441,357756102,271302126,97434765,356899539,335102382,335078557,136910650,48808029,65680141,283609518,349455328,17885048,87848163,145164178,90170106,374542136,276528870,76932259,335998405,305894929,84596290,410461584,304170356,469056321,99539659,219040184,195965227,289399271,372196563,109658022,395068425,2437540,119372899,243325458,441444928,76453988,424013028,318929008,169521089,398050432,240742729,260067679,152308875,322893842,141590129,235556719,397330616,434123961,469133393,419297826,335009260,466682342,118689745,382892423,12411005,208562033,187695282,78356791,74225061,384962065,304736474,328837677,460895056,463749181,91994564,35723770,295049334,130153730,218420406,52169952,448313827,471226577,390475462,440654817,425056226,370009307,16112872,31310283,263342070,112282990,395363597,231494851,83760761,297995314,363856033,350058290,262787122,84061929,450177112,57228049,380435284,233716660,206915637,442759732,7478594,34395745,134400521,98471464,133176742,353103078,177234411,213044610,303060055,253321572,331573192,424575800,382259129,70102432,156307305,24726556,261011706,284249405,122700235,416571533,65966729,373684937,195101901,156468066,335210240,48518042,182735096,335984073,316157617,378948469,104169590,87247290,139052241,380689908,84293184,3868024,88629395,378753937,329129732,326892889,151636810,271940355,449261285,237856363,127910202,136208273,18540059,353422148,161875694,367829083,18062469,464711536,57276742,285778999,350463251,395256184,23299754,389383680,427858195,241662939,58872248,445681951,315791469,466117569,365043752,101551490,264392633,388567408,177249608,398090200,439984433,293636940,191496423,468912407,28294927,28200409,295937837,178052916,264696238,38913227,96923457,460392860,107072502,368541340,118242850,169644863,375413848,62774739,238087409,46771092,446211773,37081927,53204617,193087659,279533514,366510457,373409789,364828899,416648961,202731554,120936630,124632769,54365581,453247245,118444038,70431642,38274432,66582918,434444849,362022230,236926063,259061944,365917738,232913908,375492182,324817218,58676208,437035339,465813733,136370591,444055196,339177264,90988643,318262134,386664994,85842556,409099061,373336259,86979520,248061530,292922774,170013482,346933277,300573968,143500008,458876218,218031452,13975065,345354860,85265335,53690935,302204300,335617959,187898226,383210505,83144442,25177453,81424223,271407733,100571291,226132143,385939957,324086105,394478384,303600596,452447253,467981189,220991354,367227418,278845325,104774813,27785734,220202998,405905338,99044090,40562164,76049956,31328668,404558734,78664148,102316475,272621585,249162105,303919775,150235723,84133770,334990952,18958937,273346160,195812579,188229201,302268816,329843230,375491549,105546671,361168506,282544917,14617852,447244338,319159459,254677850,414166256,412822964,254880344,263558402,238707938,470430018,134220841,32761103,417401628,102481492,221061366,461865394,144885781,311364699,55386662,445089986,313174288,321497535,189972252,457898188,329526206,42017905,85622176,98973026,64790994,210346162,308429222,447283264,151206126,265724528,50707313,454610905,271637094,213304774,202402898,43881680,401017026,337249935,235869647,259461799,7532265,378211337,295568070,268580278,255680331,214048442,95498527,373486815,455387729,110447568,331659833,126631800,400184396,39993304,258710259};
    cout << sol.minCost(nums2, 449844477) << endl;
    return 0;
}


/*
// @lcpr case=start
// [20,1,15]\n5\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n4\n
// @lcpr case=end

 */

